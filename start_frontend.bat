@echo off
echo Starting Resume Matcher Frontend...

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

echo Starting Streamlit frontend...
echo The application will be available at http://localhost:8501
echo Make sure the backend server is already running (start_backend.bat)
echo Press Ctrl+C to stop the application
streamlit run app/frontend/app.py 