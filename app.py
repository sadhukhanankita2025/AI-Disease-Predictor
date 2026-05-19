import streamlit as st
import pandas as pd
import numpy as np
import joblib
import base64
import io

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Personalized Healthcare",
    page_icon="🧠",
    layout="wide"
)

# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load("healthcare_model.pkl")
le = joblib.load("label_encoder.pkl")

# =========================================================
# LOAD DATA
# =========================================================

training_df = pd.read_csv("Training.csv")
med_df = pd.read_csv("medications.csv")
precautions_df = pd.read_csv("precautions_df.csv")
diet_df = pd.read_csv("diets.csv")
workout_df = pd.read_csv("workout_df.csv")

# =========================================================
# IMAGE
# =========================================================

def get_base64_image(image_path):

    with open(image_path, "rb") as img_file:

        return base64.b64encode(
            img_file.read()
        ).decode()

brain_image = get_base64_image("brain.png")

# =========================================================
# PDF REPORT
# =========================================================
def generate_report_pdf(
    patient_name,
    age,
    weight,
    height,
    bp,
    selected_symptoms,
    disease,
    medicines,
    precautions,
    diets,
    workouts
):

    import io
    from datetime import datetime

    from reportlab.platypus import (
        SimpleDocTemplate,
        Paragraph,
        Spacer,
        Table,
        TableStyle,
        KeepTogether
    )

    from reportlab.lib import colors
    from reportlab.lib.styles import (
        getSampleStyleSheet,
        ParagraphStyle
    )
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
    from reportlab.lib.units import inch

    # -----------------------------------------------------
    # CREATE BUFFER
    # -----------------------------------------------------

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=45,
        bottomMargin=45
    )

    # -----------------------------------------------------
    # STYLES
    # -----------------------------------------------------

    styles = getSampleStyleSheet()

    # Title Style
    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=28,
        leading=34,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#0f172a"),
        spaceAfter=6
    )

    # Subtitle Style
    subtitle_style = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=11,
        leading=16,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#64748b"),
        spaceAfter=20
    )

    # Section Title Style
    section_style = ParagraphStyle(
        "SectionTitle",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=16,
        leading=20,
        textColor=colors.white,
        leftIndent=8,
        spaceBefore=10,
        spaceAfter=10
    )

    # Body Style
    body_style = ParagraphStyle(
        "BodyStyle",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=11,
        leading=18,
        textColor=colors.HexColor("#111827")
    )

    # Footer Style
    footer_style = ParagraphStyle(
        "FooterStyle",
        parent=styles["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=9,
        leading=12,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#6b7280")
    )

    # Disclaimer Style
    disclaimer_style = ParagraphStyle(
        "DisclaimerStyle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=14,
        textColor=colors.HexColor("#7c2d12")
    )

    # -----------------------------------------------------
    # STORY
    # -----------------------------------------------------

    story = []

    # -----------------------------------------------------
    # HEADER
    # -----------------------------------------------------

    story.append(
        Paragraph(
            "AI Personalized Healthcare Report",
            title_style
        )
    )

    story.append(
        Paragraph(
            "Comprehensive AI-generated medical recommendation report",
            subtitle_style
        )
    )

    # Decorative line
    line = Table([[""]], colWidths=[7.0 * inch])
    line.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#2563eb")),
        ("LINEBELOW", (0, 0), (-1, -1), 0, colors.white),
    ]))
    story.append(line)
    story.append(Spacer(1, 20))

    # -----------------------------------------------------
    # PATIENT DETAILS
    # -----------------------------------------------------

    patient_name = patient_name if patient_name else "Anonymous"
    bp = bp if bp else "N/A"
    symptoms_text = ", ".join(selected_symptoms)

    # Section Header
    header = Table([[" Patient Details"]], colWidths=[7.0 * inch])
    header.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#1d4ed8")),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 15),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(header)
    story.append(Spacer(1, 8))

    info_data = [
        ["Patient Name", patient_name],
        ["Age", f"{age} Years"],
        ["Weight", f"{weight} kg"],
        ["Height", f"{height} cm"],
        ["Blood Pressure", bp],
        ["Symptoms", symptoms_text],
        ["Predicted Disease", disease],
    ]

    info_table = Table(
        info_data,
        colWidths=[180, 320]
    )

    info_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#eff6ff")),
        ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#1e3a8a")),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),

        ("BACKGROUND", (1, 0), (1, -1), colors.white),
        ("TEXTCOLOR", (1, 0), (1, -1), colors.HexColor("#111827")),

        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),

        ("VALIGN", (0, 0), (-1, -1), "TOP"),

        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))

    story.append(info_table)
    story.append(Spacer(1, 18))

    # -----------------------------------------------------
    # SECTION FUNCTION
    # -----------------------------------------------------

    def add_section(title, items):

        # Section Header Bar
        section_header = Table(
            [[title]],
            colWidths=[7.0 * inch]
        )

        section_header.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#0f172a")),
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 13),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ]))

        story.append(section_header)
        story.append(Spacer(1, 8))

        if len(items) == 0:
            story.append(
                Paragraph(
                    "No recommendations available.",
                    body_style
                )
            )
        else:
            for item in items:
                story.append(
                    Paragraph(
                        f"• {str(item)}",
                        body_style
                    )
                )
                story.append(Spacer(1, 4))

        story.append(Spacer(1, 14))

    # -----------------------------------------------------
    # SECTIONS
    # -----------------------------------------------------

    add_section("💊 Recommended Medicines", medicines)
    add_section("🛡 Precautions", precautions)
    add_section("🥗 Diet Recommendation", diets)
    add_section("🏋 Workout Plan", workouts)

    # -----------------------------------------------------
    # DISCLAIMER
    # -----------------------------------------------------

    disclaimer_table = Table(
        [[
            Paragraph(
                "<b>Medical Disclaimer:</b> "
                "This report is generated using an AI-based prediction model "
                "and is intended for informational purposes only. "
                "Please consult a qualified healthcare professional "
                "before taking any medication or making medical decisions.",
                disclaimer_style
            )
        ]],
        colWidths=[7.0 * inch]
    )

    disclaimer_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#fff7ed")),
        ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#fdba74")),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ]))

    story.append(disclaimer_table)
    story.append(Spacer(1, 24))

    # -----------------------------------------------------
    # FOOTER
    # -----------------------------------------------------

    generated_time = datetime.now().strftime("%d %B %Y, %I:%M %p")

    story.append(
        Paragraph(
            f"Generated by AI Personalized Healthcare System<br/>"
            f"Report Generated On: {generated_time}",
            footer_style
        )
    )

    # -----------------------------------------------------
    # BUILD PDF
    # -----------------------------------------------------

    doc.build(story)

    pdf = buffer.getvalue()
    buffer.close()

    return pdf

# =========================================================
# CSS
# =========================================================

st.markdown(f"""
<style>

/* =====================================================
BACKGROUND
===================================================== */

.stApp {{

    background:
    linear-gradient(
        135deg,
        #020024,
        #090979,
        #000428
    );

    color: white;

    overflow-x: hidden;
}}

#MainMenu {{
    visibility: hidden;
}}

header {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

/* =====================================================
NAVBAR
===================================================== */

.navbar {{

    background: rgba(255,255,255,0.06);

    border: 1px solid rgba(255,255,255,0.10);

    padding: 22px 40px;

    border-radius: 25px;

    backdrop-filter: blur(15px);

    margin-bottom: 40px;

    display: flex;

    justify-content: space-between;

    align-items: center;
}}

.logo {{

    font-size: 34px;

    font-weight: 800;
}}

.nav-links {{

    display: flex;

    gap: 35px;
}}

.nav-links a {{

    color: white;

    text-decoration: none;

    font-size: 18px;
}}

/* =====================================================
HERO
===================================================== */

.hero-title {{

    font-size: 72px;

    font-weight: 900;

    line-height: 1.05;
}}

.hero-title.small-title {{

    font-size: 52px;

    line-height: 1.1;
}}

.hero-title.large-title {{

    font-size: 72px;

    line-height: 1.05;
}}

.gradient-text {{

    background:
    linear-gradient(
        90deg,
        #8b5cf6,
        #06b6d4
    );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}}

.hero-sub {{

    margin-top: 20px;

    font-size: 19px;

    color: #d1d5db;

    line-height: 1.8;

    max-width: 720px;
}}

.hero-btn {{

    min-width: 280px;

    height: 60px;

    border: none;

    border-radius: 20px;

    cursor: pointer;

    font-size: 20px;

    font-weight: 800;

    color: white;

    background:
    linear-gradient(
        90deg,
        #4f46e5,
        #2563eb,
        #06b6d4
    );

    background-size: 300% 300%;

    animation: gradientMove 6s ease infinite;

    box-shadow:
    0px 0px 28px rgba(37,99,235,0.35),
    0px 0px 55px rgba(6,182,212,0.20);

    transition: 0.35s ease;
}}

.hero-btn:hover {{

    transform:
    translateY(-4px)
    scale(1.03);

    box-shadow:
    0px 0px 40px rgba(37,99,235,0.55),
    0px 0px 75px rgba(139,92,246,0.25);
}}

@keyframes gradientMove {{

    0% {{
        background-position: 0% 50%;
    }}

    50% {{
        background-position: 100% 50%;
    }}

    100% {{
        background-position: 0% 50%;
    }}
}}

.floating-image {{

    animation: floatImage 4s ease-in-out infinite;

    filter:
    drop-shadow(0px 0px 30px rgba(59,130,246,0.45))
    drop-shadow(0px 0px 60px rgba(6,182,212,0.25));
}}

@keyframes floatImage {{

    0% {{
        transform: translateY(0px);
    }}

    50% {{
        transform: translateY(-18px);
    }}

    100% {{
        transform: translateY(0px);
    }}
}}

/* =====================================================
FEATURE CARDS
===================================================== */

.feature-card {{

    min-height: 300px;

    background: rgba(255,255,255,0.08);

    border: 1px solid rgba(255,255,255,0.10);

    border-radius: 28px;

    padding: 35px;

    text-align: center;

    backdrop-filter: blur(15px);

    transition: 0.4s;
}}

.feature-card:hover {{

    transform: translateY(-10px);

    box-shadow:
    0px 0px 40px rgba(139,92,246,0.45);
}}

.card-icon {{

    font-size: 65px;

    margin-bottom: 18px;
}}

.card-title {{

    font-size: 28px;

    font-weight: 800;

    margin-bottom: 15px;
}}

.card-desc {{

    font-size: 18px;

    color: #d1d5db;

    line-height: 1.8;
}}

/* =====================================================
FORM
===================================================== */

.form-container {{

    margin-top: 40px;

    background: rgba(255,255,255,0.08);

    border-radius: 30px;

    padding: 40px;

    border: 1px solid rgba(255,255,255,0.12);

    backdrop-filter: blur(18px);
}}

.form-title {{

    font-size: 40px;

    font-weight: 900;

    margin-bottom: 12px;

    background:
    linear-gradient(
        90deg,
        #8b5cf6,
        #06b6d4
    );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}}

.form-sub {{

    color: #d1d5db;

    font-size: 18px;

    margin-bottom: 35px;
}}

/* =====================================================
INPUT FIELDS
===================================================== */

.stTextInput,
.stNumberInput,
.stDateInput,
.stMultiSelect {{

    margin-bottom: 18px;
}}

.stTextInput label,
.stNumberInput label,
.stDateInput label,
.stMultiSelect label {{

    color: #93c5fd !important;

    font-size: 18px !important;

    font-weight: 800 !important;

    letter-spacing: 0.5px;
}}

.stTextInput input,
.stNumberInput input,
.stDateInput input {{

    background:
    linear-gradient(
        145deg,
        rgba(30,64,175,0.55),
        rgba(37,99,235,0.30)
    ) !important;

    border: 1px solid rgba(96,165,250,0.45) !important;

    border-radius: 22px !important;

    color: #ffffff !important;

    height: 68px !important;

    padding-left: 20px !important;

    font-size: 18px !important;

    font-weight: 700 !important;

    backdrop-filter: blur(18px) !important;

    box-shadow:
    0 0 18px rgba(37,99,235,0.25),
    inset 0 0 10px rgba(255,255,255,0.05);

    transition: all 0.35s ease !important;
}}

.stTextInput input:focus,
.stNumberInput input:focus,
.stDateInput input:focus {{

    border:
    1px solid #38bdf8 !important;

    background:
    linear-gradient(
        145deg,
        rgba(37,99,235,0.70),
        rgba(14,165,233,0.35)
    ) !important;

    box-shadow:
    0px 0px 30px rgba(56,189,248,0.55),
    0px 0px 60px rgba(37,99,235,0.25) !important;
}}

.stMultiSelect div[data-baseweb="select"] {{

    background:
    linear-gradient(
        145deg,
        rgba(30,64,175,0.55),
        rgba(37,99,235,0.28)
    ) !important;

    border-radius: 22px !important;

    border:
    1px solid rgba(96,165,250,0.40) !important;

    min-height: 68px !important;
}}

/* =====================================================
BUTTON
===================================================== */

div.stFormSubmitButton,
div.stButton,
.stButton,
.stFormSubmitButton {{

    display: flex;

    justify-content: center;

    align-items: center;

    margin-top: 18px;
}}

div.stFormSubmitButton > button,
div.stButton > button,
.stButton > button,
button[kind="primary"] {{

    width: 320px;

    max-width: 100%;

    height: 60px;

    display: inline-flex;

    justify-content: center;

    align-items: center;

    margin: 0 auto;

    border-radius: 20px;

    border: none;

    background:
    linear-gradient(
        90deg,
        #1d4ed8,
        #2563eb,
        #3b82f6
    ) !important;

    color: white !important;

    font-size: 20px;

    font-weight: 800;

    box-shadow:
    0 14px 30px rgba(59,130,246,0.30);
}}

/* =====================================================
RESULT CARD
===================================================== */

.result-main-card {{

    background:
    linear-gradient(
        145deg,
        rgba(15,23,42,0.88),
        rgba(30,41,59,0.78)
    );

    border-radius: 35px;

    padding: 45px;

    margin-top: 40px;

    border: 1px solid rgba(255,255,255,0.10);
}}

.result-disease-title {{

    text-align: center;

    font-size: 28px;

    font-weight: 700;
}}

.result-disease-name {{

    text-align: center;

    font-size: 65px;

    font-weight: 900;

    margin-top: 15px;

    background:
    linear-gradient(
        90deg,
        #22c55e,
        #06b6d4
    );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}}

.patient-info-bar {{

    display: flex;

    justify-content: center;

    flex-wrap: wrap;

    gap: 15px;

    margin-top: 25px;
}}

.patient-pill {{

    padding: 12px 22px;

    border-radius: 50px;

    background:
    linear-gradient(
        145deg,
        rgba(30,64,175,0.45),
        rgba(37,99,235,0.22)
    );

    border: 1px solid rgba(96,165,250,0.35);

    color: #dbeafe;

    font-weight: 700;
}}

/* =====================================================
DOWNLOAD BUTTON
===================================================== */

.stDownloadButton {{

    display: flex !important;

    justify-content: center !important;
}}

.stDownloadButton button {{

    min-width: 340px !important;

    height: 72px !important;

    border-radius: 24px !important;

    border: none !important;

    background:
    linear-gradient(
        90deg,
        #8b5cf6,
        #06b6d4
    ) !important;

    color: white !important;

    font-size: 22px !important;

    font-weight: 800 !important;
}}

/* =====================================================
INFO CARDS
===================================================== */

.info-card {{

    background:
    linear-gradient(
        145deg,
        rgba(255,255,255,0.09),
        rgba(255,255,255,0.04)
    );

    border-radius: 30px;

    padding: 30px;

    border: 1px solid rgba(255,255,255,0.12);

    margin-top: 20px;
}}

.card-heading {{

    display: flex;

    align-items: center;

    gap: 15px;

    font-size: 28px;

    font-weight: 800;

    margin-bottom: 25px;
}}

.card-icon-small {{

    width: 60px;

    height: 60px;

    border-radius: 18px;

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 28px;

    background:
    linear-gradient(
        145deg,
        #8b5cf6,
        #06b6d4
    );
}}

.output-box {{

    background: rgba(255,255,255,0.07);

    border-radius: 18px;

    padding: 18px 20px;

    margin-bottom: 15px;

    border-left: 5px solid #06b6d4;

    color: #e0f2fe;

    line-height: 1.7;
}}

/* =====================================================
FOOTER
===================================================== */

.footer {{

    margin-top: 80px;

    padding: 35px;

    border-radius: 28px;

    background:
    linear-gradient(
        145deg,
        rgba(255,255,255,0.08),
        rgba(255,255,255,0.03)
    );

    border: 1px solid rgba(255,255,255,0.10);

    text-align: center;

    backdrop-filter: blur(15px);
}}

.footer-title {{

    font-size: 28px;

    font-weight: 900;

    margin-bottom: 12px;

    background:
    linear-gradient(
        90deg,
        #8b5cf6,
        #06b6d4
    );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}}

.footer-text {{

    color: #cbd5e1;

    font-size: 17px;

    line-height: 1.8;
}}

.footer-copy {{

    margin-top: 18px;

    color: #94a3b8;

    font-size: 15px;
}}

h1,h2,h3,h4,h5,h6,p,label {{
    color: white !important;
}}

</style>
""", unsafe_allow_html=True)

# =========================================================
# NAVBAR
# =========================================================

st.markdown("""
<div class="navbar">

<div class="logo">
🧠 Healthcare AI
</div>

<div class="nav-links">

<a href="#home">Home</a>

<a href="#predict">Predict</a>

<a href="#report">Download Report</a>

</div>

</div>
""", unsafe_allow_html=True)

# =========================================================
# HERO SECTION
# =========================================================

col1, col2 = st.columns([1.15,1])

with col1:

    st.markdown("""
    <div id="home">

    <div class="hero-title small-title">
    AI-Powered
    </div>

    <div class="hero-title gradient-text large-title">
    Personalized<br>
    Healthcare
    </div>

    <div class="hero-sub">

    Advanced AI healthcare recommendation system for disease prediction,
    medicines, precautions, personalized diet plans, workout suggestions,
    and premium downloadable medical reports.

    </div>

    <div style="
    margin-top:35px;
    display:flex;
    justify-content:center;
    ">

    <a href="#predict">

    <button class="hero-btn">

    🚀 Start AI Health Analysis

    </button>

    </a>

    </div>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div style="
    display:flex;
    justify-content:center;
    align-items:center;
    ">

    <img class="floating-image"
    src="data:image/png;base64,{brain_image}"
    style="
    width:620px;
    height:420px;
    object-fit:cover;
    border-radius:32px;
    ">

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# FORM
# =========================================================

st.markdown('<div id="predict"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="form-container">

<div class="form-title">
👤 Patient Information
</div>

<div class="form-sub">
Fill patient details and symptoms for AI disease prediction.
</div>
""", unsafe_allow_html=True)

with st.form("healthcare_form"):

    col1, col2 = st.columns(2)

    with col1:

        patient_name = st.text_input("Patient Name")

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120
        )

        weight = st.number_input(
            "Weight (kg)",
            min_value=1
        )

    with col2:

        height = st.number_input(
            "Height (cm)",
            min_value=1
        )

        bp = st.text_input("Blood Pressure")

        appointment_date = st.date_input(
            "Appointment Date"
        )

    symptoms = training_df.columns[:-1]

    selected_symptoms = st.multiselect(
        "Select Symptoms",
        symptoms
    )

    submitted = st.form_submit_button(
        "🚀 AI Health Check"
    )

st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# PREDICTION
# =========================================================

if submitted:

    if len(selected_symptoms) == 0:

        st.warning("⚠ Please select symptoms.")

    else:

        input_data = np.zeros(len(symptoms))

        for symptom in selected_symptoms:

            index = list(symptoms).index(symptom)

            input_data[index] = 1

        input_data = input_data.reshape(1, -1)

        prediction = model.predict(input_data)

        disease = le.inverse_transform(prediction)[0]

        medicines = med_df[
            med_df["Disease"] == disease
        ]["Medication"].values

        precautions_raw = precautions_df[
            precautions_df["Disease"] == disease
        ].iloc[:,1:].values.flatten()

        precautions = [
            p for p in precautions_raw
            if str(p) != "nan"
        ]

        diets = diet_df[
            diet_df["Disease"] == disease
        ]["Diet"].values

        workouts = workout_df[
            workout_df["disease"] == disease
        ]["workout"].values

        st.markdown(f"""
        <div class="result-main-card">

        <div class="result-disease-title">
        🩺 AI Predicted Disease
        </div>

        <div class="result-disease-name">
        {disease}
        </div>

        <div class="patient-info-bar">

        <div class="patient-pill">
        👤 {patient_name or 'Anonymous'}
        </div>

        <div class="patient-pill">
        🎂 {age} Years
        </div>

        <div class="patient-pill">
        ⚖ {weight} kg
        </div>

        <div class="patient-pill">
        📏 {height} cm
        </div>

        <div class="patient-pill">
        🩸 BP: {bp or 'N/A'}
        </div>

        </div>

        <div class="info-card">

        <div class="card-heading">
        <div class="card-icon-small">💊</div>
        Recommended Medicines
        </div>

        <div class="output-box">
        {"<br>".join(medicines) if len(medicines) > 0 else "No medicines found for this condition."}
        </div>

        </div>

        <div class="info-card">

        <div class="card-heading">
        <div class="card-icon-small">🥗</div>
        Diet Recommendation
        </div>

        <div class="output-box">
        {"<br>".join(diets) if len(diets) > 0 else "No diet recommendations available."}
        </div>

        </div>

        <div class="info-card">

        <div class="card-heading">
        <div class="card-icon-small">🏋</div>
        Workout Plan
        </div>

        <div class="output-box">
        {"<br>".join(workouts) if len(workouts) > 0 else "No workout plan available."}
        </div>

        </div>

        <div class="info-card">

        <div class="card-heading">
        <div class="card-icon-small">🛡</div>
        Precautions
        </div>

        <div class="output-box">
        {"<br>".join(precautions) if len(precautions) > 0 else "No precautions available."}
        </div>

        </div>

        </div>
        """, unsafe_allow_html=True)

        report_bytes = generate_report_pdf(
            patient_name,
            age,
            weight,
            height,
            bp,
            selected_symptoms,
            disease,
            medicines,
            precautions,
            diets,
            workouts
        )

        st.markdown('<div id="report"></div>', unsafe_allow_html=True)

        st.download_button(
            label="📄 Download Premium Report",
            data=report_bytes,
            file_name="healthcare_report.pdf",
            mime="application/pdf"
        )

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

<div class="footer-title">
🧠 AI Personalized Healthcare
</div>

<div class="footer-text">

Advanced AI-powered healthcare recommendation system
for disease prediction, medicines, precautions,
diet plans, workout suggestions, and premium reports.

</div>

<div class="footer-copy">

© 2026 AI Healthcare System • Built with Streamlit & AI

</div>

</div>
""", unsafe_allow_html=True)