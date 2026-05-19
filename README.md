# 🩺 AI Disease Predictor (Smart Healthcare System)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![Machine Learning](https://img.shields.io/badge/ML-Powered-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

An AI-powered healthcare web application that predicts possible diseases based on user symptoms and provides personalized medical guidance, including medicines, precautions, diet plans, workout suggestions, and downloadable reports.

---

## 📌 Features

### 🧠 Smart Disease Prediction
- Predict diseases using a trained ML model  
- Accept multiple symptoms as input  
- Fast and accurate results  

### 💊 Medical Recommendations
- Suggested medicines  
- Safety precautions  
- Doctor-style guidance  

### 🥗 Health & Lifestyle Guidance
- Personalized diet plans  
- Workout recommendations  
- Recovery improvement tips  

### 📄 PDF Health Report
- Downloadable medical report  
- Includes prediction + recommendations  
- Professional format  

### 🎨 Modern UI
- Clean Streamlit interface  
- Card-based layout  
- Easy symptom selection  

---

## 🛠️ Tech Stack

- 🐍 Python  
- 🎈 Streamlit  
- 📊 Pandas, NumPy  
- 🤖 Scikit-learn  
- 💾 Joblib  
- 📄 ReportLab  

---
## 📁 Project Structure
HEALTHCARE-AI/
│
├── app.py
├── brain.png
├── image.png
├── diets.csv
├── medications.csv
├── precautions_df.csv
├── workout_df.csv
├── Training.csv
├── healthcare_model.pkl
├── label_encoder.pkl
├── requirements.txt
└── README.md
---

## ⚙️ Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/AI-Disease-Predictor.git
cd AI-Disease-Predictor

2️⃣ Create Virtual Environment
python -m venv venv

Activate:

Windows:

venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run App
streamlit run app.py

🧠 How It Works
User selects symptoms
Data is preprocessed
ML model predicts disease
System generates:
💊 Medicines
🛡️ Precautions
🥗 Diet plan
🏋️ Workout plan
User downloads PDF report

📊 Example Output
Predicted Disease: Diabetes

💊 Medicines:
- Metformin
- Insulin (if required)

🛡️ Precautions:
- Avoid sugar intake
- Monitor glucose levels

🥗 Diet:
- High fiber foods
- Low carbs

🏋️ Workout:
- Walking 30 mins daily

📸 Project Screenshots
 🏠 Home Page
 <p align="center"> <img src="assets/image.png" width="700"/> </p>
  
 🧠 Prediction Page
 <p align="center"> <img src="assets/image2.png" width="700"/> </p>

 📄 Report Page
 <p align="center"> <img src="assets/image3.png" width="700"/> </p> <p align="center"> <img src="assets/image4.png" width="700"/> </p> <p align="center"> <img src="assets/image5.png" width="700"/> </p>
 