from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV2025.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Eduardo Padron"
PAGE_ICON = ":wave:"
NAME = "Eduardo Padron"
DESCRIPTION = """
Data-cloud engineer, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "padrondata@gmail.com"
SOCIAL_MEDIA = {
    "Medium blog": "https://medium.com/@fulldataalchemist",
    "LinkedIn": "www.linkedin.com/in/padrondata", ##cambiar
    "GitHub": "https://github.com/fullmakeralchemist",
}

PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 4 years of experience extracting actionable insights from data to drive informed business decisions
- ✔️ Strong hands on experience and knowledge in AWS, Python SQL and Excel
- ✔️ Experienced in transforming raw data into actionable insights and impactful dashboards
- ✔️ Skilled in ETL development and building data engineering solutions using AWS services
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Pandas, Pyspark), SQL
- 📊 Data Visulization: Power Bi, Streamlit, Plotly
- ⚙️ Data Engineering & Cloud Tools: AWS Glue, Lambda, AppFlow, Transfer Family, SageMaker, Textract, Personalize and more
- 🤖 ML & Prototyping: Classification models and computer vision in Python with Raspberry Pi & Arduino integrations
- 🗄️ Databases: PostgreSQL, MariaDB, MySQL, Redshift, Athena
"""
)


#chance quitar lo de abajo

# --- Projects & Accomplishments ---
#st.write('\n')
#st.subheader("Projects & Accomplishments")
#st.write("---")
#for project, link in PROJECTS.items():
#    st.write(f"[{project}]({link})")"
