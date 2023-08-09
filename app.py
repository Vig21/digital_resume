from pathlib import Path
import streamlit as st
from PIL import Image

#cwd is for jupyter notebooks in the same path
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "VIGNESH_RESUME.pdf"
profile_pic = current_dir / "assets" / "profile.png"


#-- General Info ---
PAGE_TITLE = "Digital CV | Vignesh Tallam" #page_name
PAGE_ICON = ":wave:"  #:random:
NAME = "Vignesh Tallam"
DESCRIPTION = """
Data Scientist, assisting enterprises by making data implementable!.
"""
EMAIL = "vigsach@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/vigneshtallam/",
    "GitHub": "https://github.com/Vig21",
    "Leetcode":"https://leetcode.com/vigsach/"
}
#! needs to be modified later
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
# st.title("Testing here!!!") ---- to check if webpage is displaying
#---Load assets like pic,resume--
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True) #to link to css_file in the same folder
with open(resume_file, "rb") as pdf_file: #pic
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


#---About section--
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230) #adjust pixels based on pic

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream", #find out about this...
    )
    st.write("📫", EMAIL)

#---Adding social media links on the web page
st.write('#')
cols = st.columns(len(SOCIAL_MEDIA)) # social media dictionary has all the links
for index, (platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


#---Experience and Qualifications--
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 6 months experience building Python scripts to scrape and automate tasks, visualise data to make it actionable
- ✔️ Strong hands on experience and knowledge in Python and SQL
- ✔️ Good understanding to build scalable cloud environments and infrastructure in AWS and Azure
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: Tableau, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Cloud Engineer-I | Persistent Systems**")
st.write("11/2022 - Present")
st.write(
    """
- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

#--- Job 2
st.write("🚧", "**Data Science Intern | AMBEE (Google Tech⭐)**")
st.write("01/2022 - 09/2022 ")
st.write(
    """
- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")

st.write("Gold Medalist for the term 2018-2022")
st.write("Best Outgoing student (Department) for 2022")

for project,links in PROJECTS.items(): #need to customise to point to uni project and work on Github
    st.write(f"[{project}]({links})") #links are within tuples