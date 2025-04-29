from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app import gemini_service
from typing import Dict, Optional

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
    token_usage: Optional[Dict] = None

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
    - Token usage information (if available)
    """
    try:
        result = gemini_service.analyze_resume_for_job(
            request.job_description, 
            request.resume
        )
        
        # If the result is a tuple with analysis and token usage
        if isinstance(result, tuple) and len(result) == 2:
            analysis, token_usage = result
            return AnalysisResponse(analysis=analysis, token_usage=token_usage)
        
        # If just a string is returned (for backward compatibility)
        return AnalysisResponse(analysis=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)