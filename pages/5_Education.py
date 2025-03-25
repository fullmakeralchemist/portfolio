from pathlib import Path
import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Education | Eduardo Padron"
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

# --- Projects ---
# --- WORK HISTORY ---
st.write('\n')
st.subheader("Previous Education")
st.write("---")

# --- JOB 1
st.write("🚧", "**Universidad de Guanajuato | Master in Water Sciences**")
st.write("Graduated in 2021")
st.write(
    """
- ► Technological community coordinator
- ► Developed a small-scale irrigation system project, including programming, 3D modeling, and hardware integration.
- ► Participated in multiple events and competitions focused on technology, open-source development, and data applications.
- ► Collaborated on patent documentation and prototyping for innovative water management technologies.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Universidad de Guanajuato | Bachelor in Hydraulic Engineering**")
st.write("Graduated in 2018")
st.write(
    """
- ► Led the development of an automated rain simulation system, integrating programming, hardware components, and 3D modeling for controlled environmental testing.
- ► Engaged in various tech-focused events and hackathons, contributing to open-source projects and data-driven solutions.
- ► Contributed to water infrastructure projects involving data analysis for rainfall patterns, pipe system efficiency, and simulation-based decision-making.
"""
)  

# --- JOB 3
st.write('\n')
st.write("🚧", "**Universidade da Coruña | Master Investigation Intership research data and IT**")
st.write("2019")
st.write(
    """
- ► Research work in CITEEC (Technological innovation center in construction and civil engineering) and CITIC (Information and communication technology research center).
- ► Utilized SQL, Python, and MQTT to automate and enhance data processing, visualization, and real-time analysis for an automatic irrigation system. 
- ► Architected and implemented a platform for Data Collection to satisfy reporting, data science, and analytics needs.
- ► Supervised the design and development of new data warehouses.
- ► Created 3D printing tools and fixtures to reduce costs and enable scalability.
"""
)
#meterle el certificado

# --- SKILLS ---
st.write('\n')
st.subheader("Binational Academic Projects")
st.write(
    """
- 👩‍💻 -Comtemporary issues in water resouces U.S - Mexico water, food energy nexus. Texas A&M University/University of Guanajuato. (2017). 
- 📊 U.S.-Mexico bidirectional study abroad program in water supported by 100,000 strong in America´s. Gateway Community College/University of Guanajuato.(2017). 
- ⚙️ -2nd International workshop on hydrologic and hydrogeochemical processes in inter-montane Basins. Texas A&M University, College Station, Texas, EE. UU. (2019_.

"""
)