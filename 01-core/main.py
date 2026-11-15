import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from google import genai
from google.genai import errors

load_dotenv()
app = FastAPI()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


class Question(BaseModel):
    question: str = Field(min_length=1)


@app.post("/ask")
async def ask(body: Question):
    try:
        response = await client.aio.models.generate_content(
            model="gemini-3.8-flash",
            contents=body.question,
        )
    except errors.ServerError:
        raise HTTPException(
            status_code=503,
            detail="The AI service is busy. Please try again in a moment.",
        )
    return {"answer": response.text}