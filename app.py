
import streamlit as st
from pdfextractor import text_extractor
from langchain_google_genai import ChatGoogleGenerativeAI

import os
# First lets configure the model 
gemini_app_key=os.getenv('GOOGLE_API_KEY1')
model=ChatGoogleGenerateAI(
    model='gemini-2.5-flash-lite',
    api_key=gemini_api_key,
    temperature=0.9,
)

# Let's create the side bar to upload the resume 

st.sidebar.title(':red[UPLOAD YOUR RESUME (Only PDF)]')
file=st.sidebar.file_uploader('Resume',type=['pdf'])
if file: 
    file_text=text_extractor(file)
st.sidebar.success('Resume Uploaded Successfully')

# Create the main page of the application
st.title(":orange[SKILLMATCH:-]:blue[AI Assisted Skill Matching Tool]")


st.markdown('### :green [This application helps you to match and analyze your resume with the job description by the use of AI]')
tips='''
Follow these steps:-
1.Upload your resume (PDF Only) in side bar
2. Copy and paste the job Description below.
3. Click on submit the run the application '''

st.write(tips)

job_desc=st.text_area(':red[Copy and paste your job description over here]')
if st.button('SUBMIT'):

    prompt=f'''
    <role> You are an expert career coach and resume analyzer.
    <goal> Your task is to compare a applicant's resume with a job description provided by the applicant.
    <context> The following content is the applicant's resume:
    * Resume : {file_text}
    * Job Description : {job_desc}
    <format> The report should follow these steps
    * Give a brief description of applicant in 3 to 5 lines. 
    * Describe in percentage what are the chances of this resume getting selected for the job role(give approximate).
    * Need not to be exact percentage  you can give interval of percentage like 70-80%.
    * Give the expected ATS score along with matching and non-matching keywords.
    * Perform SWOT analysis and explain each parameter that is strength,weakness,opportunity and threat in detail.
    * Give what all current resume that are required to be added or removed to match the job description.
    * Show both and current version of resume and modified or improved version of resume after analyzing with job description.
    <Instruction>
    * Use bullet points for explanation where ever possible.
    * Create tables for describtion where ever required.
    * strictly do not add any new skill in sample resume.
    * The format od Sample Resume shoulb be in such a way that it can be copied and pasted directly in words.
    '''

    response=model.invoke(prompt)
    st.write(response.content)
