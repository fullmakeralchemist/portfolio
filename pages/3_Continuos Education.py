import streamlit as st

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Certifications | Eduardo Padron"
PAGE_ICON = ":wave:"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Achievements mapped to PDF filenames
CERTIFICATES = {
    "🏆 English C1 TOEFL ITP ": "certificates/TOEFL.pdf",
    "🏆 ML Ops Course": "certificates/Curso de MLOps.pdf",
    "🏆 Data Engineering Bootcamp": "certificates/Jose Eduardo Padron Ramirez BID.pdf",
    "🏆 Data Analysis Bootcamp": "certificates/Certificado - Bootcamp de Análisis de Datos.pdf",
    "🏆 Python Advanced Bootcamp": "certificates/Certificado - Bootcamp de Python Avanzado.pdf",
    "🏆 Python Course": "certificates/PythonCodigoFacilito.pdf",
    "🏆 Data Science Bootcamp": "certificates/Jose Eduardo Padron Ramirez BCD.pdf",
    "🏆 Advanced Data Science Bootcamp": "certificates/Jose Eduardo Padron Ramirez BCDA.pdf",
    "🏆 Edx Analyzing Data with Excel": "certificates/edx_excel.pdf",
    "🏆 Open Data and Civic Hacking Course": "certificates/LABLEON_DATOSABIERTOS_RECONOCIMIENTO.pdf",
    "🏆 Azure AI-900": "certificates/AI900.pdf",
    "🏆 WOBI in leadership Medellín, Colombia": "certificates/WOBI Certificado José Padrón.pdf",
    #"🏆 Data Science Bootcamp": "assets/CV.pdf",
    #"🏆 Data Science Bootcamp": "assets/CV.pdf",
}

#st.set_page_config(page_title="Certifications / Training", page_icon="🏆")

st.subheader("Certifications / Training")
st.write("---")

for title, file_path in CERTIFICATES.items():
    with open(file_path, "rb") as file:
        st.download_button(
            label=title,
            data=file,
            file_name=file_path,
            mime="application/pdf"
        )
