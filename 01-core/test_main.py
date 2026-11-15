from types import SimpleNamespace
from fastapi.testclient import TestClient
import main

api = TestClient(main.app)


async def fake_generate_content(model, contents):
    return SimpleNamespace(text="fake answer")


def make_fake_gemini():
    models = SimpleNamespace(generate_content=fake_generate_content)
    return SimpleNamespace(aio=SimpleNamespace(models=models))


def test_ask_returns_answer(monkeypatch):
    monkeypatch.setattr(main, "client", make_fake_gemini())
    response = api.post("/ask", json={"question": "Hello"})
    assert response.status_code == 200
    assert response.json() == {"answer": "fake answer"}


def test_wrong_type_is_rejected():
    response = api.post("/ask", json={"question": 123})
    assert response.status_code == 422


def test_empty_question_is_rejected():
    response = api.post("/ask", json={"question": ""})
    assert response.status_code == 422