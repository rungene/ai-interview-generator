from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

# 1. Properly load environment variables from your .env file
load_dotenv()

# GEMINI_API_KEY=your_key inside .env file
API_KEY = os.getenv('GEMINI_API_KEY')
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Initialize the client
client = genai.Client(api_key=API_KEY)


class JobRequest(BaseModel):
    title: str


# Test if API is working
@app.get("/")
def home():
    return {"message": "AI Interview Generator API is running"}


@app.post("/generate")
def generate_questions(data: JobRequest):

    # structured instructions help parsing later
    prompt = f"""
    Generate exactly 3 thoughtful interview questions for a {data.title} role.
    Make them professional, specific, and focused on real job situations.
    Return only the questions separated by newlines, with no markdown styling
    or numbering.
    """

    # 3. Use the valid production model
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    # 4. Access response text
    content = response.text

    questions = [
        q.strip()
        for q in content.split("\n")
        if q.strip()
    ]

    return {"questions": questions[:3]}  # slice to get exactly 3 elements
