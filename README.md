# Resume Matcher with Gemini API
## GDSC NED Workshop Project

This project helps you match your resume with job descriptions to identify gaps and improve your resume for specific job applications. Perfect for students and job seekers looking to tailor their resumes for better results!

## Features

- Upload a job description
- Upload your resume
- Get AI-powered analysis of the match between your resume and the job description
- Receive suggestions for improving your resume

## Prerequisites

- Python 3.8+
- Google API key for Gemini

## Setup Instructions

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/resume-matcher.git
   cd resume-matcher
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Get a Google API key for Gemini:
   - Go to [Google AI Studio](https://makersuite.google.com/)
   - Create a new API key
   - Copy the API key
   - See GEMINI_API_SETUP.md for detailed instructions

5. Create a `.env` file and add your API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Running the Application

1. Start the FastAPI backend:
   ```
   uvicorn app.main:app --reload
   ```

2. In a separate terminal, start the Streamlit frontend:
   ```
   streamlit run app/frontend/app.py
   ```

3. Open your browser and navigate to `http://localhost:8501` to use the application

## Project Structure

```
resume-matcher/
├── app/
│   ├── main.py              # FastAPI main application
│   ├── gemini_service.py    # Gemini API integration
│   └── frontend/
│       └── app.py           # Streamlit frontend
├── sample_data/             # Sample job descriptions and resumes
├── .env                     # Environment variables (not tracked by git)
├── env.example              # Example environment file
├── GEMINI_API_SETUP.md      # Instructions for getting Gemini API key
├── WORKSHOP_GUIDE.md        # Guide for workshop instructors
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

## How It Works

1. The user uploads a job description and their resume through the Streamlit interface
2. The FastAPI backend sends this information to the Gemini API
3. Gemini analyses the match and provides suggestions
4. The results are displayed to the user in a user-friendly format

## Workshop Details

This project is designed for the GDSC NED Gemini API Workshop. During the workshop, we'll explore:

- How to integrate with Google's Gemini API
- Building a backend API with FastAPI
- Creating a frontend with Streamlit
- Prompt engineering for effective AI interactions

For workshop instructors, please refer to WORKSHOP_GUIDE.md for detailed session planning.

## What You'll Learn

- Working with Google's Gemini API for text analysis
- Building a RESTful API with FastAPI
- Creating interactive web interfaces with Streamlit
- The fundamentals of prompt engineering for AI
- Integrating frontend and backend components
- Managing environment variables for API keys

## Extending the Project

Here are some ideas to enhance this project after the workshop:

1. Add file upload support for PDFs and Word documents
2. Implement user authentication
3. Add a database to store analysis history
4. Create a visualization of skills matching
5. Generate a new optimized resume based on suggestions
6. Add support for multiple job descriptions comparison

## Workshop Resources

- [Presentation Slides](https://example.com/workshop-slides)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)

## Credits

This project was created for the GDSC NED Gemini API Workshop.

## License

MIT License