from fastapi import FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from app import gemini_service

app = FastAPI(title="Resume Matcher API")

# Add CORS middleware to allow cross-origin requests from the Streamlit app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalysisRequest(BaseModel):
    job_description: str
    resume: str

class AnalysisResponse(BaseModel):
    analysis: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Resume Matcher API"}

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_resume(request: AnalysisRequest):
    """
    Analyze a resume for a specific job description using Gemini AI.
    
    Parameters:
    - job_description: The full text of the job description
    - resume: The full text of the resume
    
    Returns:
    - Analysis and suggestions for improving the resume
    """
    try:
        analysis = gemini_service.analyze_resume_for_job(
            request.job_description, 
            request.resume
        )
        return AnalysisResponse(analysis=analysis)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# For form-based submissions (optional)
@app.post("/analyze-form", response_model=AnalysisResponse)
async def analyze_resume_form(
    job_description: str = Form(...),
    resume: str = Form(...)
):
    try:
        analysis = gemini_service.analyze_resume_for_job(job_description, resume)
        return AnalysisResponse(analysis=analysis)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)