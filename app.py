from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app = Flask(__name__)

IMG_SIZE = (224,224)

model = tf.keras.models.load_model("mobilenetv2_best.keras")

class_names = [
"Apple___Apple_scab","Apple___Black_rot","Apple___Cedar_apple_rust","Apple___healthy",
"Blueberry___healthy",
"Cherry___Powdery_mildew","Cherry___healthy",
"Corn___Cercospora_leaf_spot Gray_leaf_spot","Corn___Common_rust","Corn___Northern_Leaf_Blight","Corn___healthy",
"Grape___Black_rot","Grape___Esca_(Black_Measles)","Grape___Leaf_blight_(Isariopsis_Leaf_Spot)","Grape___healthy",
"Orange___Haunglongbing_(Citrus_greening)",
"Peach___Bacterial_spot","Peach___healthy",
"Pepper,_bell___Bacterial_spot","Pepper,_bell___healthy",
"Potato___Early_blight","Potato___Late_blight","Potato___healthy",
"Raspberry___healthy",
"Soybean___healthy",
"Squash___Powdery_mildew",
"Strawberry___Leaf_scorch","Strawberry___healthy",
"Tomato___Bacterial_spot","Tomato___Early_blight","Tomato___Late_blight",
"Tomato___Leaf_Mold","Tomato___Septoria_leaf_spot","Tomato___Spider_mites Two-spotted_spider_mite",
"Tomato___Target_Spot","Tomato___Tomato_Yellow_Leaf_Curl_Virus",
"Tomato___Tomato_mosaic_virus","Tomato___healthy"
]

def predict_image(img_path):

    img = Image.open(img_path).convert("RGB")
    img = img.resize(IMG_SIZE)
    img = np.array(img)/255.0
    img = np.expand_dims(img,axis=0)

    prediction = model.predict(img)
    index = np.argmax(prediction)

    return class_names[index]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/upload",methods=["GET","POST"])
def upload():

    if request.method=="POST":

        file = request.files["file"]

        if file:

            path="static/images/upload.jpg"
            file.save(path)

            result=predict_image(path)

            return render_template("result.html",
                                   result=result,
                                   img=path)

    return render_template("upload.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)