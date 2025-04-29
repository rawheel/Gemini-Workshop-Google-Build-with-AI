import streamlit as st
import requests
import os

# Configure the page
st.set_page_config(
    page_title="Resume Matcher",
    page_icon="📝",
    layout="wide",
)

# Load sample data files
def load_sample_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except Exception as e:
        st.error(f"Error loading {filename}: {str(e)}")
        return ""

# API endpoint
API_URL = "http://localhost:8080/analyze"

# App header
st.title("📝 Resume Matcher with Gemini AI")
st.markdown("""
This tool analyzes your resume against a specific job description to identify key skills and suggest improvements.
""")

# Load sample data
sample_job = load_sample_file("sample_data/sample_job_description.txt")
sample_resume = load_sample_file("sample_data/sample_resume.txt")

# Create two columns for job description and resume
col1, col2 = st.columns(2)

with col1:
    st.subheader("Job Description")
    job_description = st.text_area(
        "Job Description",
        value=sample_job,
        height=300
    )

with col2:
    st.subheader("Your Resume")
    resume = st.text_area(
        "Resume",
        value=sample_resume,
        height=300
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
                    
                    st.subheader("Analysis Results")
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
                st.info("Make sure the FastAPI backend is running on port 8080")

# Footer
st.caption("Created for Gemini API Workshop - GDSC NED") 