import streamlit as st
import requests
import json

# Configure the page
st.set_page_config(
    page_title="Resume Matcher",
    page_icon="📝",
    layout="wide",
)

# API endpoint (update if your API runs on a different URL)
API_URL = "http://localhost:8080/analyze"

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .subheader {
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    .result-header {
        font-size: 1.8rem;
        margin: 1.5rem 0 1rem 0;
    }
    .skill-highlight {
        background-color: #f0f8ff;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .footer {
        margin-top: 3rem;
        text-align: center;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# App header
st.markdown("<h1 class='main-header'>📝 Resume Matcher with Gemini AI</h1>", unsafe_allow_html=True)
st.markdown("""
This tool analyzes your resume against a specific job description to:
- Identify key skills required for the job
- Check if your resume demonstrates these skills
- Suggest improvements to better match the job requirements
""")

# Create two columns for job description and resume
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h2 class='subheader'>Job Description</h2>", unsafe_allow_html=True)
    job_description = st.text_area(
        "Paste the job description here",
        height=300,
        placeholder="Copy and paste the full job description here...",
        label_visibility="collapsed"
    )

with col2:
    st.markdown("<h2 class='subheader'>Your Resume</h2>", unsafe_allow_html=True)
    resume = st.text_area(
        "Paste your resume here",
        height=300,
        placeholder="Copy and paste your resume text here...",
        label_visibility="collapsed"
    )

# Submit button
if st.button("Analyze Resume", type="primary", use_container_width=True):
    if not job_description or not resume:
        st.error("Please provide both a job description and your resume.")
    else:
        with st.spinner("Analyzing your resume with Gemini AI..."):
            try:
                # Send data to API
                response = requests.post(
                    API_URL,
                    json={"job_description": job_description, "resume": resume},
                    headers={"Content-Type": "application/json"}
                )
                
                if response.status_code == 200:
                    # Display results
                    result = response.json()
                    analysis = result.get("analysis", "")
                    
                    st.markdown("<h2 class='result-header'>Analysis Results</h2>", unsafe_allow_html=True)
                    
                    # Format the response for better readability
                    st.markdown(analysis)
                    
                    # Add an option to download the analysis
                    st.download_button(
                        label="Download Analysis",
                        data=analysis,
                        file_name="resume_analysis.txt",
                        mime="text/plain"
                    )
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Failed to connect to the API: {str(e)}")
                st.info("Make sure the FastAPI backend is running (uvicorn app.main:app --reload)")

# Add sample data expander
with st.expander("Sample Data (For Testing)"):
    st.subheader("Sample Job Description")
    sample_job = """
    Job Title: Junior Python Developer
    
    Company: Tech Innovations Inc.
    
    Requirements:
    - Bachelor's degree in Computer Science or related field
    - 1-2 years of experience with Python programming
    - Knowledge of web frameworks such as FastAPI or Flask
    - Experience with database systems (SQL, PostgreSQL)
    - Familiarity with RESTful APIs
    - Basic understanding of front-end technologies (HTML, CSS, JavaScript)
    - Good problem-solving skills and attention to detail
    - Excellent communication and teamwork abilities
    
    Responsibilities:
    - Develop and maintain Python applications
    - Collaborate with cross-functional teams to define and design new features
    - Write clean, efficient, and maintainable code
    - Troubleshoot and debug applications
    - Implement security and data protection measures
    - Integrate user-facing elements with server-side logic
    - Participate in code reviews and team meetings
    """
    if st.button("Use Sample Job Description"):
        st.code(sample_job)
        st.session_state.sample_job = sample_job
    
    st.subheader("Sample Resume")
    sample_resume = """
    John Doe
    johndoe@email.com | (123) 456-7890 | github.com/johndoe
    
    EDUCATION
    Bachelor of Science in Information Technology
    University of Technology, Graduated May 2022
    
    SKILLS
    - Programming Languages: JavaScript, Java, Python (basic)
    - Web Development: HTML, CSS, React
    - Tools: Git, VS Code, Jira
    - Databases: MySQL
    
    EXPERIENCE
    Web Developer Intern | TechStart Company | June 2022 - Present
    - Developed responsive web pages using HTML, CSS, and JavaScript
    - Assisted in maintaining the company's WordPress website
    - Participated in weekly team meetings and sprint planning
    - Created documentation for internal web applications
    
    IT Support Assistant | University IT Department | Sept 2020 - May 2022
    - Provided technical support to students and faculty
    - Troubleshot hardware and software issues
    - Maintained inventory of IT equipment
    - Assisted in setting up computer labs for classes
    
    PROJECTS
    Personal Blog Website
    - Created a blog website using HTML, CSS, and JavaScript
    - Implemented responsive design for mobile compatibility
    - Hosted on GitHub Pages
    
    Inventory Management System
    - Developed a simple inventory tracking system using Java
    - Created a MySQL database to store product information
    - Implemented basic CRUD functionality
    """
    if st.button("Use Sample Resume"):
        st.code(sample_resume)
        st.session_state.sample_resume = sample_resume

# Apply sample data if available
if hasattr(st.session_state, 'sample_job') and not job_description:
    job_description = st.session_state.sample_job
if hasattr(st.session_state, 'sample_resume') and not resume:
    resume = st.session_state.sample_resume

# Footer
st.markdown("<div class='footer'>Created for Gemini API Workshop - GDSC NED</div>", unsafe_allow_html=True) 