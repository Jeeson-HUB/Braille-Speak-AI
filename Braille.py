from flask import Flask, render_template, request
import time
import os, sys

sys.path.insert(0, 'final_model')
from final_model.space_recognition_original import make_prediction

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home.html')

@app.route("/upload")
def upload():
    return render_template('upload.html')


@app.route("/upload_results", methods=['GET', 'POST'])
def save():
    # Save the image in the path
    if request.method == 'POST' and 'fileField' in request.files:
        s = request.files['fileField']
        filename = s.save(r"D:\Corezone\2024-2025\Checkings\Braille\static\a.jpg")

    img_path = r"D:\Corezone\2024-2025\Checkings\Braille\static\a.jpg"
    predicted_letter = make_prediction(img_path)
    print(predicted_letter, "jo")
    return render_template('display.html', filename=filename, letter=predicted_letter)


if __name__ == "__main__":
    app.run(debug=True)
