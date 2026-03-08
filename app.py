from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load model
model = tf.keras.models.load_model("mobilenetv2_best.keras")

IMG_SIZE = (224,224)

# Class labels
classes = [
"Apple___Apple_scab",
"Apple___Black_rot",
"Apple___Cedar_apple_rust",
"Apple___healthy",
"Blueberry___healthy",
"Cherry___Powdery_mildew",
"Cherry___healthy",
"Corn___Cercospora_leaf_spot",
"Corn___Common_rust",
"Corn___Northern_Leaf_Blight",
"Corn___healthy",
"Grape___Black_rot",
"Grape___Esca",
"Grape___Leaf_blight",
"Grape___healthy",
"Orange___Citrus_greening",
"Peach___Bacterial_spot",
"Peach___healthy",
"Pepper___Bacterial_spot",
"Pepper___healthy",
"Potato___Early_blight",
"Potato___Late_blight",
"Potato___healthy",
"Raspberry___healthy",
"Soybean___healthy",
"Squash___Powdery_mildew",
"Strawberry___Leaf_scorch",
"Strawberry___healthy",
"Tomato___Bacterial_spot",
"Tomato___Early_blight",
"Tomato___Late_blight",
"Tomato___Leaf_Mold",
"Tomato___Septoria_leaf_spot",
"Tomato___Spider_mites",
"Tomato___Target_Spot",
"Tomato___Yellow_Leaf_Curl_Virus",
"Tomato___Mosaic_virus",
"Tomato___healthy"
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")
import os

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["image"]

    filename = file.filename
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    file.save(filepath)

    img = Image.open(filepath).convert("RGB")
    img = img.resize((224,224))

    img_array = np.array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    index = np.argmax(prediction)

    result = classes[index]

    plant, condition = result.split("___")

    return render_template(
        "result.html",
        plant=plant,
        condition=condition,
        image_path=filename
    )
if __name__ == "__main__":
    app.run(debug=True)