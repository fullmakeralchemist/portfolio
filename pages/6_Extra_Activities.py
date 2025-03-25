from pathlib import Path
import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Extras | Eduardo Padron"
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



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# Achievements mapped to PDF filenames
WORKSHOPS = {
    "🏆 Developed and implemented workshop for Science Clubs International to teach AI as a tool for sustainable development with Python.": "certificates/CV.pdf",
    "🏆 Electronics with art workshop for kids at OSHWDem by Bricolabs (Spain)": "certificates/CV.pdf",
    #"🏆 Python Advanced Bootcamp": "assets/CV.pdf",
    #"🏆 Data Science Bootcamp": "assets/CV.pdf",
    #"🏆 Data Science Bootcamp": "assets/CV.pdf",
}

st.subheader("Workshop Instructor")
st.write("---")

for title, file_path in WORKSHOPS.items():
    with open(file_path, "rb") as file:
        st.download_button(
            label=title,
            data=file,
            file_name=file_path,
            mime="application/pdf"
        )
    
# --- Projects ---
# --- WORK HISTORY ---
st.write('\n')
st.subheader("Extra activities")
st.write("---")

# --- JOB 1
st.write("🚧", "**Future Lab | Community member**")
st.write("2017 - Present")
st.write(
    """
- ► Technological community focused on scientific and technological innovation, project development, organization of events and educational initiatives.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Bricolabs | Community member remote in Spain**")
st.write("2019 - Present")
st.write(
    """
- ► Community focused on designing and collaborating with the Open Source movement, the ethics of DIY and the culture of development in free technologies.
"""
)  