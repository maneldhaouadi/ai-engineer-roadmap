import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from google import genai

load_dotenv()                                        # reads .env
app = FastAPI()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class Question(BaseModel):                           # the security guard
    question: str

@app.post("/ask")                                    # POST = sending data
async def ask(body: Question):                       # async = don't freeze
    response = await client.aio.models.generate_content(   # await = wait
        model="gemini-3.8-flash",
        contents=body.question,
    )
    return {"answer": response.text}