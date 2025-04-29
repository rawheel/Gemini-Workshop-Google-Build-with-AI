#!/bin/bash

# Activate virtual environment if it exists
if [ -d "venv" ]; then
  echo "Activating virtual environment..."
  source venv/bin/activate
else
  echo "Virtual environment not found. Please create one first:"
  echo "python -m venv venv"
  echo "source venv/bin/activate  # On Windows: venv\\Scripts\\activate"
  echo "pip install -r requirements.txt"
  exit 1
fi

# Check if required packages are installed
if ! pip show fastapi uvicorn > /dev/null 2>&1; then
  echo "Installing required packages..."
  pip install -r requirements.txt
fi

# Start the FastAPI backend
echo "Starting FastAPI backend server..."
echo "The server will be available at http://localhost:8000"
echo "Press Ctrl+C to stop the server"
uvicorn app.main:app --reload 