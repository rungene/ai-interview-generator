# AI Interview Question Generator

A simple AI-powered web application that generates thoughtful interview questions based on a job title.

## Overview

This application allows users to enter a job title (for example, `Customer Success Manager`) and generates 3 professional interview questions tailored to that role using the Gemini API.

---

## Features

- Generate role-specific interview questions
- Simple and clean UI
- Loading spinner during AI generation
- Smart input handling on successful generation
- Error handling for invalid requests
- FastAPI backend
- Vanilla HTML/CSS/JavaScript frontend

---

## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- FastAPI
- Uvicorn

### AI
- Gemini API

---

## Project Structure

```bash
├── main.py
├── requirements.txt
├── index.html
├── .env.example       
└── README.md
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd ai-interview-generator
```

---

### 2. Create a Virtual Environment

#### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---
### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key
```

---

## Running the Application

### Start the FastAPI Backend

```bash
uvicorn main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

---

### Open the Frontend

Open `index.html` directly in the browser

OR

run a local server:

```bash
python -m http.server 5500
```

Then visit:

```text
http://localhost:5500
```

---

## API Endpoint

### POST `/generate`

Generate interview questions for a given role.

#### Request Body

```json
{
  "title": "Customer Success Manager"
}
```

#### Example Response

```json
{
  "questions": [
    "How would you handle a customer threatening to churn due to onboarding delays?",
    "Describe a time you turned around a difficult customer relationship.",
    "How do you balance customer advocacy with company revenue goals?"
  ]
}
```

---

## Notes

- API keys are stored using environment variables and are not hardcoded.
- CORS is enabled to allow frontend-backend communication during development.
- The application uses Gemini's language model to generate context-aware interview questions.

---

## Future Improvements

- Add question difficulty levels
- Add role categories
- Improve UI responsiveness
- Save previous generations
- Add streaming responses

---

## Author

Built as part of a coding assessment project.