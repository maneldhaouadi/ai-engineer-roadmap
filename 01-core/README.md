# Phase 1: Ask API

A FastAPI endpoint that sends a question to Gemini and returns the answer.

## Run
pip install -r requirements.txt
uvicorn main:app --reload

## Test
pytest

## What I learned
- API, POST, async/await
- Pydantic validation (422 errors)
- Keeping keys in .env, never in Git
- CI with GitHub Actions