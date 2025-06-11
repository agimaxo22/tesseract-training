from flask import Flask, render_template, request
from PIL import Image
import pytesseract
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_text = ''
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            extracted_text = pytesseract.image_to_string(Image.open(filepath))
    return render_template('index.html', text=extracted_text)

if __name__ == '__main__':
    app.run(debug=True)

