import streamlit as st

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Work Experience | Eduardo Padron"
PAGE_ICON = ":wave:"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work Experience")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Engineer | Grupo Traxion**")
st.write("09/2023 - Present")
st.write(
    """
- ► Designed, developed, and maintained end-to-end ETL pipelines using AWS services to extract data from diverse sources such as Salesforce, SAP, and various APIs, transforming it for analysis, dashboarding and reporting purposes.
- ► Supported machine learning development by assisting in the deployment of ML models with AWS SageMaker and contributed to the creation of a chatbot proof of concept (POC) to deliver internal data insights, driving innovation in data accessibility and usage.
- ► Collaborated on a document processing project using AWS Textract to extract and structure data from physical documents, supporting the creation of a searchable internal database for operational efficiency.
- ► Conducted  training sessions for junior team members on AWS services, data pipelines, and job monitoring techniques, ensuring team proficiency in executing data-related tasks effectively.
- ► Performed data analysis on processed datasets to support business decision-making and validate data pipeline outputs, ensuring alignment with enterprise projects and objectives.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Manager (Data Analyst) | City Cancer Challenge**")
st.write("08/2021 - 06/2023")
st.write(
    """
- ► Monitor quality of needs assessment data inputted using pre-defined indicators.
- ► Support development of needs assessment summary reports and analytics using C/Can data platform.
- ► Facilitate discussions around data management and analysis with local stakeholders.
- ► Support throughout the needs assessment data project in 3 cities from different countries to ensure data completeness, accuracy, quality, standardizing reporting, data insights and data visualisation as outlined in the C/Can Responsible Data Framework.
- ► Played a key role in data collection, analysis, and visualization by integrating data from distinct databases using SQL. 
- ► Gathered information from diverse sources, to create visually compelling and interactive dashboards, providing stakeholders with intuitive insights into critical areas of cancer care. 
- ► Utilized data visualization tools and techniques to present complex information in a user-friendly manner, enabling informed decision-making and fostering a deeper understanding of the data.
"""
)  

# --- JOB 3
st.write('\n')
st.write("🚧", "**IoT Engineering/ Data Scientist  (Investigation Role) | Universidad de Guanajuato**")
st.write("01/2018 - 12/2021")
st.write(
    """
- ► Implemented an automated irrigation project with open source platforms.
- ► Utilized SQL, Python, and MQTT to automate and enhance data processing, visualization, and real-time analysis for an automatic irrigation system. 
- ► Architected and implemented a platform for Data Collection to satisfy reporting, data science, and analytics needs.
- ► Supervised the design and development of new data warehouses.
- ► Created 3D printing tools and fixtures to reduce costs and enable scalability.
"""
)

# Achievements mapped to PDF filenames
VOL1 = {
    "🏆 Junior ML Engineer Omdena - Dryad Certificate": "certificates/Omdena Certificate_Eduardo Padron.pdf",
    #"🏆 Electronics with art workshop for kids at OSHWDem by Bricolabs (Spain)": "assets/CV.pdf",
    #"🏆 Python Advanced Bootcamp": "assets/CV.pdf",
    #"🏆 Data Science Bootcamp": "assets/CV.pdf",
    #"🏆 Data Science Bootcamp": "assets/CV.pdf",
}

# Achievements mapped to PDF filenames
VOL2 = {
    "🏆 Junior Data Engineer Ploomber Project": "https://www.linkedin.com/posts/ploomber_ploomber-hacktoberfest-project-showcase-activity-7125497336339795969-h_Uf?utm_source=share&utm_medium=member_android&rcm=ACoAADUHEIMB8WCQwZm8IAIMsMHiis5ueHJdPFE",
    #"🏆 Electronics with art workshop for kids at OSHWDem by Bricolabs (Spain)": "assets/CV.pdf",
    #"🏆 Python Advanced Bootcamp": "assets/CV.pdf",
    #"🏆 Data Science Bootcamp": "assets/CV.pdf",
    #"🏆 Data Science Bootcamp": "assets/CV.pdf",
}

st.subheader("Volunteer Experience")
st.write("---")

# --- Volunteer 1
st.write('\n')
st.write("🚧", "**Junior ML Engineer | Omdena - Dryad**")
st.write("09/2021 - 11/2021 (U.S.A.)")
st.write(
    """
- ► Implemented a complete pipeline for detecting forest fires applying supervised machine learning techniques. The Python pipeline included Data Analysis for Anomaly Detection, Data Quality check and Preprocessing modules, training and inference of multiple Classification models and further deployment in Docker containers.
"""
)

for title, file_path in VOL1.items():
    with open(file_path, "rb") as file:
        st.download_button(
            label=title,
            data=file,
            file_name=file_path,
            mime="application/pdf"
        )

# --- Volunteer 2
st.write('\n')
st.write("🚧", "**Junior Data Engineer | Ploomber**")
st.write("09/2023 - 11/2023 (U.S.A.)")
st.write(
    """
- ► Ploomber team guidance to develop a production-ready project using Data Engineering (ETL pipelines with SQL and Python) for Data Analysis, Storytelling, and Visualization.
"""
)

# --- Accomplishments ---
#st.write('\n')
#st.write("---")
for project, link in VOL2.items():
    st.write(f"[{project}]({link})")