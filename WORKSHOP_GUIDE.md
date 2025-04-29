# Resume Matcher Workshop Guide

This guide is designed for instructors leading the Gemini API workshop. It provides step-by-step instructions to help students build the Resume Matcher application.

## Workshop Objectives

By the end of this workshop, students will:
1. Understand how to integrate Gemini AI into a web application
2. Learn to build a backend API with FastAPI
3. Create a user interface with Streamlit
4. Implement prompt engineering for a specific use case

## Prerequisites

Ensure all students have:
- Python 3.8+ installed
- A Google account to access Gemini API
- Basic understanding of Python programming
- Git installed (optional, for cloning the repository)

## Workshop Timeline (3 hours)

| Time | Activity |
|------|----------|
| 0:00 - 0:20 | Introduction and Setup |
| 0:20 - 0:50 | Understanding the Project Architecture |
| 0:50 - 1:20 | Implementing the Gemini API Service |
| 1:20 - 1:50 | Building the FastAPI Backend |
| 1:50 - 2:20 | Creating the Streamlit Frontend |
| 2:20 - 2:50 | Testing and Improvements |
| 2:50 - 3:00 | Q&A and Conclusion |

## Detailed Workshop Plan

### Introduction and Setup (20 minutes)

1. **Welcome and Introduction** (5 minutes)
   - Introduce yourself and the workshop objectives
   - Explain what Gemini AI is and its capabilities
   - Overview of the project we'll be building

2. **Environment Setup** (15 minutes)
   - Guide students to clone the repository
   - Help them set up a virtual environment
   - Install dependencies
   - Get Google API key for Gemini (follow GEMINI_API_SETUP.md)

### Understanding the Project Architecture (30 minutes)

1. **Project Overview** (10 minutes)
   - Explain the project structure
   - Review the technologies: FastAPI, Streamlit, Gemini AI
   - Discuss the data flow: Frontend → Backend → Gemini API

2. **Code Walkthrough** (20 minutes)
   - Review the main components:
     - `app/gemini_service.py`: Gemini API integration
     - `app/main.py`: FastAPI backend
     - `app/frontend/app.py`: Streamlit frontend
   - Explain prompt engineering for Gemini

### Implementing the Gemini API Service (30 minutes)

1. **Understanding the Gemini API** (10 minutes)
   - Explain Google's generative AI library
   - Discuss model options and capabilities
   - Review authentication and API request structure

2. **Prompt Engineering** (20 minutes)
   - Explain the importance of effective prompts
   - Discuss the specific prompt for resume matching
   - Guide students to modify the prompt for better results

### Building the FastAPI Backend (30 minutes)

1. **FastAPI Introduction** (10 minutes)
   - Key features of FastAPI
   - API endpoints and request/response models
   - Async functionality

2. **Implementing the API** (20 minutes)
   - Guide students through the main.py code
   - Explain the API endpoints and their functions
   - Show how to connect the Gemini service to the API

### Creating the Streamlit Frontend (30 minutes)

1. **Streamlit Introduction** (10 minutes)
   - Key features of Streamlit
   - Building UI components
   - State management

2. **Frontend Implementation** (20 minutes)
   - Guide students through the app.py code
   - Explain the UI components and their functions
   - Show how to connect the frontend to the API

### Testing and Improvements (30 minutes)

1. **Testing the Application** (15 minutes)
   - Run the backend and frontend
   - Test with sample data
   - Debug common issues

2. **Enhancing the Application** (15 minutes)
   - Discuss potential improvements
   - Encourage students to customize the application
   - Show examples of UI enhancements

### Q&A and Conclusion (10 minutes)

1. **Open Discussion**
   - Answer questions from students
   - Discuss challenges and solutions

2. **Next Steps**
   - Suggest ways to extend the project
   - Share resources for further learning
   - Collect feedback on the workshop

## Troubleshooting Common Issues

1. **API Key Issues**
   - Ensure the .env file is correctly set up
   - Check for typos in the API key
   - Verify API quota hasn't been exceeded

2. **Package Installation Problems**
   - Make sure students are using the correct Python version
   - Check for conflicting dependencies
   - Suggest upgrading pip if needed

3. **Connection Issues**
   - Ensure backend is running before starting frontend
   - Check port availability
   - Verify network permissions

4. **Frontend Display Issues**
   - Explain Streamlit's rendering process
   - Check browser compatibility
   - Suggest clearing cache if needed

## Additional Resources

- [Gemini AI Documentation](https://ai.google.dev/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

## After the Workshop

Encourage students to:
1. Extend the project with additional features
2. Share their versions on GitHub
3. Experiment with different prompts
4. Try different AI models and compare results

## Feedback Collection

Consider creating a short feedback form to gather insights on:
- Workshop pace and content
- Areas of confusion
- Most valuable parts
- Suggestions for future workshops 