from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")


@app.get("/")
def home():
    return {"status": "bot running"}


@app.post("/webhook")
async def webhook(req: Request):
    data = await req.form()

    incoming_msg = data.get("Body", "")

    response = requests.post(
        "https://api.mistral.ai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {MISTRAL_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "mistral-small-latest",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "Tu es un assistant WhatsApp professionnel, "
                        "court, poli et utile."
                    ),
                },
                {
                    "role": "user",
                    "content": incoming_msg,
                },
            ],
        },
    )

    ai_reply = response.json()["choices"][0]["message"]["content"]

    twiml = f"""
    <Response>
        <Message>{ai_reply}</Message>
    </Response>
    """

    return twiml
