import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Gemini API
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Set up the model
model = genai.GenerativeModel('gemini-1.5-pro-002')

def analyze_resume_for_job(job_description, resume):
    """
    Analyze the resume in context of the job description using Gemini API.
    
    Args:
        job_description (str): The job description text
        resume (str): The resume text
        
    Returns:
        str: Analysis and suggestions from Gemini
    """
    prompt = f"""
    I'm going to give you a job description and my resume. Please:

    1. Identify the top 3-5 MUST-HAVE skills from the job description.
    
    2. For each bullet point on my resume, pinpoint the specific skill it demonstrates. 
       If a bullet point isn't relevant to the job, please let me know.
    
    3. If my resume doesn't strongly reflect a MUST-HAVE skill, suggest specific 
       rewrites to my bullet points to better showcase it. Use keywords and phrases 
       from the job description. Also while giving the suggestions, give what should 
       be the better point to add in to my resume.

    JOB DESCRIPTION:
    {job_description}

    MY RESUME:
    {resume}
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error analyzing resume: {str(e)}" 