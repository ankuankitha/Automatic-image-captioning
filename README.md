# Image Captioning Web Application

## Overview
This is a Flask-based web application that generates image captions using a deep learning model. It takes an image input from the user, processes it using the **ViT-GPT2 image captioning model**, and returns a generated caption.

## Features
- Upload an image and receive an AI-generated caption.
- Uses **Hugging Face's ViT-GPT2 model** for caption generation.
- Responsive UI with image preview before submission.
- Flask backend with a simple web interface using HTML, CSS, and Bootstrap.

## Technologies Used
- **Python** (Flask, Torch, Transformers, PIL)
- **Hugging Face Transformers** (ViT-GPT2 model for image captioning)
- **Flask** (Web framework)
- **HTML/CSS/Bootstrap** (Frontend design)

## Installation & Setup
### 1. Clone the Repository
```bash
git clone <repo_url>
cd Image-Captioning-Web-Application
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```bash
pip install flask torch transformers pillow
```

### 4. Run the Flask Application
```bash
python app.py
```
The server should start at `http://127.0.0.1:5000/`.

## Project Structure
```
/Image-Captioning-Web-Application
│── app.py           # Flask backend
│── /templates
│   ├── index.html   # Frontend UI
│── /static
│   ├── style.css    # Stylesheet
```

## How It Works
1. **Upload an Image**: Select an image file from your computer.
2. **Generate Caption**: The model processes the image and generates a caption.
3. **View the Result**: The predicted caption appears on the web page.

## Example
**Input:** Image of a dog running in a field
**Output:** "A dog is running through a grassy field."

## Troubleshooting
### "jinja2.exceptions.TemplateNotFound: index.html"
- Ensure `index.html` is inside the `templates/` folder.
- Restart the Flask server after making any changes.
```bash
python app.py
```

### "ModuleNotFoundError: No module named 'flask'"
- Install dependencies:
```bash
pip install flask
```

## License
This project is open-source and free to use.

---
**Happy Captioning! 🖼️✨**



![image](https://github.com/user-attachments/assets/c02fb8c3-28c6-4732-a2d1-65354bb5c45a)
![image](https://github.com/user-attachments/assets/09118a5b-3a90-4a94-a14b-8fc0520b1253)
