from flask import Flask, render_template, request
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
from deep_translator import GoogleTranslator
import easyocr
import numpy as np
import nltk
from nltk.corpus import names

nltk.download("names")

app = Flask(__name__)

device = "cuda" if torch.cuda.is_available() else "cpu"
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large").to(device)
reader = easyocr.Reader(["en"])  # OCR Reader for English

INDIAN_LANGUAGES = ["hi", "bn", "te", "mr", "ta", "ur", "gu", "ml", "kn", "pa", "or", "as", "ma", "ne", "si"]
COMMON_NAMES = set(names.words())

def generate_caption(image):
    inputs = blip_processor(image, return_tensors="pt").to(device)
    output = blip_model.generate(**inputs, max_length=20, num_beams=5, temperature=1.0, top_k=50)
    caption = blip_processor.decode(output[0], skip_special_tokens=True).strip()
    return caption

def extract_bold_and_names(image):
    image_np = np.array(image)
    results = reader.readtext(image_np, detail=1)  # Get details including bbox and confidence
    
    bold_texts = []
    detected_names = []
    
    for (bbox, text, confidence) in results:
        if confidence > 0.7:  # Assume higher confidence means bold/prominent text
            bold_texts.append(text)
        if text in COMMON_NAMES:  # Check if detected text is a common name
            detected_names.append(text)
    
    bold_text = " ".join(bold_texts) if bold_texts else "No bold text found"
    name_text = ", ".join(detected_names) if detected_names else "No names detected"
    
    return bold_text, name_text

@app.route("/")
def index():
    return render_template("index.html", prediction=None, subtitle=None, bold_text=None, name_info=None)

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files.get("file")
    language = request.form.get("language", "hi")
    
    if not file or not file.content_type.startswith("image"):
        return "Invalid file. Please upload an image."
    
    if language not in INDIAN_LANGUAGES:
        language = "hi"

    image = Image.open(file.stream).convert("RGB")
    caption = generate_caption(image)
    bold_text, name_info = extract_bold_and_names(image)

    translated_caption = GoogleTranslator(source="auto", target=language).translate(caption)
    english_caption = GoogleTranslator(source="auto", target="en").translate(caption)

    return render_template("index.html", 
                           prediction=f"📸 {translated_caption}", 
                           subtitle=f"(English: {english_caption})",
                           bold_text=f"Bold Text: {bold_text}",
                           name_info=f"Detected Names: {name_info}")

if __name__ == "__main__":
    app.run(debug=True)
