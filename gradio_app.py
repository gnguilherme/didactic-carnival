import random
import time
import uuid

import gradio as gr
import requests

API_URL = "http://api:8000/"


def start_conversation(user_id: str, messages: list):
    response = requests.post(
        API_URL + "conversations/", json={"user_id": user_id, "message": messages}
    )
    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to start conversation"}


def update_conversation(user_id: str, message: list):
    response = requests.post(API_URL + f"update/{user_id}", json={"message": message})
    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to update conversation"}


def get_bot_message():
    return random.choice(["How are you?", "Today is a great day", "I'm very hungry"])


def respond(message: str, chat_history: list):
    global user_id
    chat_history.append({"role": "user", "content": message})
    chat_history.append({"role": "assistant", "content": get_bot_message()})
    time.sleep(2)
    update_conversation(user_id=user_id, message=chat_history)
    return "", chat_history


def launch_gradio_app():
    # Initialize the conversation

    with gr.Blocks() as demo:
        global user_id
        user_id = str(uuid.uuid4())
        chatbot = gr.Chatbot(type="messages")
        msg = gr.Textbox()
        clear = gr.ClearButton([msg, chatbot])
        start_conversation(user_id=user_id, messages=chatbot.value)
        msg.submit(respond, [msg, chatbot], [msg, chatbot])

        print(user_id)
        print(chatbot.value)

    demo.launch(server_name="0.0.0.0")


if __name__ == "__main__":
    launch_gradio_app()
