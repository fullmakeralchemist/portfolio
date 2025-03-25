from pathlib import Path
import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Projects | Eduardo Padron"
PAGE_ICON = ":wave:"
NAME = "Eduardo Padron"
DESCRIPTION = """
Data-cloud engineer, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "padrondata@gmail.com"
SOCIAL_MEDIA = {
    "Medium": "https://medium.com/@fulldataalchemist",
    "LinkedIn": "www.linkedin.com/in/padrondata", ##cambiar
    "GitHub": "https://github.com/fullmakeralchemist",
}

PROJECTS = {
    "✌️ Hands Spelling Recognition with Object Detection App - Object detection model": "https://fulldataalchemist.medium.com/building-your-own-real-time-object-detection-app-roboflow-yolov8-and-streamlit-part-1-f577cf0aa6e5",
    "📊 Needs Assessment Patient Perspective": "https://github.com/fullmakeralchemist/data_analysis_bootcamp",
    "🤖 Tiny ML in interactive spaces Arduino X K-WAY Challenge Project": "https://projecthub.arduino.cc/fullmakeralchemist/tiny-ml-in-interactive-spaces-arduino-x-k-way-challenge-project-original-version-d88430",
    "🗄️ Weather Data Collection": "https://github.com/fullmakeralchemist/dataengweather",
    "📊 Data Insights and Real-Time Predictive Analytics with Streamlit": "https://github.com/fullmakeralchemist/weather_prediction",
    "🗄️ Transforming a Company through Building a ETL for Data Analysis with Ploomber": "https://www.linkedin.com/posts/ploomber_ploomber-hacktoberfest-project-showcase-activity-7125497336339795969-h_Uf?utm_source=share&utm_medium=member_android&rcm=ACoAADUHEIMB8WCQwZm8IAIMsMHiis5ueHJdPFE",
    "🏆 Mapping dance AI project google": "https://experiments.withgoogle.com/collection/tfliteformicrocontrollers",
    #"🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://github.com/fullmakeralchemist/dataengweather",
    #"🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://github.com/fullmakeralchemist/dataengweather",
}

ACHIVEMENTS = {
    "🏆 Winner of the TensorFlow Microcontoller Challenge, with ML movement model for Mapping with dance Movements. Google (2021)": "https://blog.tensorflow.org/2021/10/announcing-winners-of-tensorflow-lite.html",
    "🏆 Data Camp Portofolio Challenge (2023)": "https://www.instagram.com/datacamp/p/CyV-P8vtYdZ/?img_index=2",
    "🏆 1st place UBSA Human Excellence and Social Responsibility award. Guanajuato, Mexico (2018)": "https://www.ugto.mx/noticias/noticias/14255-fomentan-responsabilidad-social-de-estudiantes-de-la-ug-con-el-premio-ubsa",
    "🏆 Municipal youth award of the government of the city of Guanajuato. Guanajuato, Mexico (2018).": "",
    #"🏆 Data Insights and Real-Time Predictive Analytics with Streamlit": "https://github.com/fullmakeralchemist/weather_prediction",
    #"🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://github.com/fullmakeralchemist/dataengweather",
    #"🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://github.com/fullmakeralchemist/dataengweather",
    #"🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://github.com/fullmakeralchemist/dataengweather",
    #"🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://github.com/fullmakeralchemist/dataengweather",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- Projects ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- Accomplishments ---
st.write('\n')
st.subheader("Accomplishments")
st.write("---")
for project, link in ACHIVEMENTS.items():
    st.write(f"[{project}]({link})")