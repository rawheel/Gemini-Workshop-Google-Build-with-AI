import os
import google.generativeai as genai
from dotenv import load_dotenv
from typing import Tuple, Dict, Optional, Union

# Load environment variables
load_dotenv()

# Configure the Gemini API
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# LLM Configuration - Edit these parameters to control generation
LLM_CONFIG = {
    "model": "gemini-1.5-pro-002",   # Model name
    "temperature": 0.2,              # Lower for more deterministic results (0.0-1.0)
    "max_output_tokens": 2048,       # Maximum number of tokens to generate
    "top_p": 0.9,                    # Nucleus sampling probability, The AI ranks all possible next words by probability
    "top_k": 40,                     # The model can only choose from the 40 most likely next words
}


# Set up the model with configuration
model = genai.GenerativeModel(
    model_name=LLM_CONFIG["model"],
    generation_config={
        "temperature": LLM_CONFIG["temperature"],
        "max_output_tokens": LLM_CONFIG["max_output_tokens"],
        "top_p": LLM_CONFIG["top_p"],
        "top_k": LLM_CONFIG["top_k"],
    }
)

def analyze_resume_for_job(job_description: str, resume: str) -> Union[str, Tuple[str, Dict[str, int]]]:
    """
    Analyze the resume in context of the job description using Gemini API.
    
    Args:
        job_description (str): The job description text
        resume (str): The resume text
        
    Returns:
        Union[str, Tuple[str, Dict[str, int]]]: 
            Either just the analysis text (for backward compatibility)
            or a tuple of (analysis text, token usage dictionary)
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
        
        # Get token usage if available
        usage_metadata = None
        if hasattr(response, 'usage_metadata'):
            usage_metadata = {
                'prompt_token_count': response.usage_metadata.prompt_token_count,
                'candidates_token_count': response.usage_metadata.candidates_token_count,
                'total_token_count': response.usage_metadata.total_token_count
            }
            print(f"Token usage: {usage_metadata}")
            
            # Return both the analysis and token usage
            return response.text, usage_metadata
            
        # For backward compatibility, return just the text
        return response.text
    except Exception as e:
        return f"Error analyzing resume: {str(e)}" 