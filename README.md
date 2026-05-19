# 🩺 AI Disease Predictor (Smart Healthcare System)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![Machine Learning](https://img.shields.io/badge/ML-Powered-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

An AI-powered **healthcare web application** that predicts possible diseases based on user symptoms and provides **personalized medical guidance**, including medicines, precautions, diet plans, workout suggestions, and downloadable reports.

---

## 🚀 Live Demo
*(If deployed, add your link here)*  
👉 https://your-streamlit-app-link.com

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
AI-Disease-Predictor/
│
├── app.py # Main Streamlit application
├── model.pkl # Trained ML model
├── symptoms_dict.pkl # Symptom mapping (if used)
├── label_encoder.pkl # Encoded labels
├── requirements.txt # Project dependencies
├── README.md # Project documentation
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
