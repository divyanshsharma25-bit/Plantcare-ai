# 🌿 PlantCare AI

AI-powered **Plant Disease Detection System** built using **Deep Learning (MobileNetV2)** and **Flask**.

This application allows users to upload a plant leaf image and instantly detect whether the plant is **healthy or affected by disease**.

---

# 🚀 Features

✔ Upload plant leaf images
✔ AI detects plant disease instantly
✔ Identifies plant type and condition
✔ Clean and responsive web interface
✔ Built using MobileNetV2 deep learning model

---

# 🧠 AI Model

The system uses **MobileNetV2**, a lightweight Convolutional Neural Network designed for efficient image classification.

Dataset used:

**New Plant Diseases Dataset (Augmented)**

The model can detect **38 different plant disease classes** including:

* Apple Scab
* Tomato Leaf Mold
* Corn Rust
* Potato Blight
* Healthy Plants

---

# 🖥️ Tech Stack

### Backend

* Python
* Flask

### Machine Learning

* TensorFlow
* Keras
* MobileNetV2

### Frontend

* HTML
* CSS

### Libraries

* NumPy
* Pillow

---

# 📂 Project Structure

```
plantcare-ai
│
├── app.py
├── mobilenetv2_best.keras
├── requirements.txt
│
├── templates
│   ├── home.html
│   ├── about.html
│   ├── upload.html
│   └── result.html
│
├── static
│   ├── style.css
│   └── uploads
│
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```
git clone https://github.com/divyanshsharma25-bit/Plantcare-ai.git
```

Go to project folder

```
cd Plantcare-ai
```

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
python app.py
```

Open in browser

```
http://127.0.0.1:5000
```

---

# 📷 How It Works

1️⃣ Upload a plant leaf image
2️⃣ Image is processed by the AI model
3️⃣ The model predicts the disease class
4️⃣ Results are displayed with plant name and condition

---

# 📊 Model Training

Training includes:

* Image augmentation
* Transfer learning using MobileNetV2
* EarlyStopping
* ReduceLROnPlateau

These techniques improve model accuracy and prevent overfitting.

---

# 🌱 Future Improvements

* Add treatment suggestions for diseases
* Display prediction confidence score
* Deploy the application online
* Mobile application support

---

# 👨‍💻 Author

**Divyansh Sharma**

B.Tech Student
AI / Machine Learning Enthusiast

---
