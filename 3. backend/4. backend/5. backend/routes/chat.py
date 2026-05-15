from fastapi import APIRouter

router = APIRouter()

@router.post("/chat")
def chat(message: dict):

    user_message = message.get("message")

    return {
        "response": f"Jarvis received: {user_message}"
    }
