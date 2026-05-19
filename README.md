# 🩺 AI Disease Predictor (Smart Healthcare System)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![Machine Learning](https://img.shields.io/badge/ML-Powered-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

An AI-powered **healthcare web application** that predicts possible diseases based on user symptoms and provides **personalized medical guidance**, including medicines, precautions, diet plans, workout suggestions, and downloadable reports.


---

## 📌 Features

### 🧠 Smart Disease Prediction
- Predicts diseases using trained Machine Learning model
- Accepts multiple symptoms as input
- Fast and accurate predictions

### 💊 Medical Recommendations
- Suggested medicines for predicted disease
- Safe usage precautions
- Doctor-style recommendations

### 🥗 Health & Lifestyle Guidance
- Personalized diet plan
- Daily workout suggestions
- Recovery improvement tips

### 📄 PDF Health Report
- Generate downloadable medical report
- Includes prediction + all recommendations
- Professional healthcare format

### 🎨 Modern UI
- Clean Streamlit interface
- Card-based layout
- Easy-to-use dropdown symptom selection

---

## 🛠️ Tech Stack

- 🐍 Python
- 🎈 Streamlit
- 📊 Pandas, NumPy
- 🤖 Scikit-learn
- 💾 Joblib (Model serialization)
- 📄 ReportLab (PDF generation)

---

## 📁 Project Structure
HEALTHCARE-AI/
│
├── __pycache__/             # Compiled Python bytecode files
├── app.py                   # Main application entry point (Streamlit/Flask/FastAPI)
├── brain.png                # Asset/Image used in the application UI
├── diets.csv                # Dataset containing dietary recommendations
├── healthcare_model.pkl     # Trained machine learning model file
├── image.png                # Asset/Image used in the application UI
├── label_encoder.pkl        # Pickle file for encoding/decoding categorical labels
├── medications.csv          # Dataset containing medication recommendations
├── precautions_df.csv       # Dataset containing medical precaution details
├── README.md                # Project documentation (this file)
├── requirements.txt         # List of Python dependencies and packages
├── Training.csv             # Dataset used for training the model
└── workout_df.csv           # Dataset containing workout/exercise recommendations
---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/AI-Disease-Predictor.git
cd AI-Disease-Predictor
2️⃣ Create Virtual Environment
python -m venv venv

Activate it:

Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Application
streamlit run app.py
🧠 How It Works
User selects symptoms from dropdown menu
Data is preprocessed using encoders
ML model predicts possible disease
System generates:
💊 Medicines
🛡️ Precautions
🥗 Diet plan
🏋️ Workout plan
User downloads full health report (PDF)
📊 Example Output
Predicted Disease: Diabetes
--------------------------------
💊 Medicines:
- Metformin
- Insulin (as prescribed)

🛡️ Precautions:
- Avoid sugar intake
- Regular blood sugar monitoring

🥗 Diet Plan:
- High fiber foods
- Low carb diet

🏋️ Workout:
- Walking 30 mins daily
- Light cardio exercises
📸 UI Preview
 ## 📸 Project Screenshots

### 🏠 Home Page
<p align="center">
  <img src="assets/image.png" width="700"/>
</p>

---

### 🧠 Prediction Page
<p align="center">
  <img src="assets/image2.png" width="700"/>
</p>

---

### 📄 Report Page

<p align="center">
  <img src="assets/image3.png" width="700"/>
</p>

<p align="center">
  <img src="assets/image4.png" width="700"/>
</p>

<p align="center">
  <img src="assets/image5.png" width="700"/>
</p>