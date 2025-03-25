import streamlit as st

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Certifications | Eduardo Padron"
PAGE_ICON = ":wave:"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Achievements mapped to PDF filenames
CERTIFICATES = {
    "🏆 English C1 TOEFL ITP ": "certificates/CV.pdf",
    "🏆 Data Analysis Bootcamp": "certificates/CV.pdf",
    "🏆 Python Advanced Bootcamp": "certificates/CV.pdf",
    "🏆 Python Course": "certificates/CV.pdf",
    "🏆 Data Science Bootcamp": "certificates/CV.pdf",
    "🏆 Advanced Data Science Bootcamp": "certificates/CV.pdf",
    "🏆 Edx Analyzing Data with Excel": "certificates/CV.pdf",
    "🏆 Open Data and Civic Hacking Course": "certificates/CV.pdf",
    "🏆 Azure AI-900": "certificates/CV.pdf",
    "🏆 WOBI in leadership Medellín, Colombia": "certificates/CV.pdf",
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
