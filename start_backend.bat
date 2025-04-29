@echo off
echo Starting Resume Matcher Backend...

IF EXIST venv (
    echo Activating virtual environment...
    call venv\Scripts\activate
) ELSE (
    echo Virtual environment not found. Please create one first:
    echo python -m venv venv
    echo venv\Scripts\activate
    echo pip install -r requirements.txt
    exit /b 1
)

echo Starting FastAPI backend server...
echo The server will be available at http://localhost:8000
echo Press Ctrl+C to stop the server
uvicorn app.main:app --reload 