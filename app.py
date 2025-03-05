from fastapi import FastAPI
import tensorflow as tf
import numpy as np
import random
import json
import nltk
import pickle
from nltk.stem import WordNetLemmatizer
from pydantic import BaseModel
from datetime import datetime as dt
from fastapi.middleware.cors import CORSMiddleware

import streamlit as st
import requests

# Load Model and Data
model = tf.keras.models.load_model("./functions/chatbot_model.h5")
words = pickle.load(open("./functions/words.pkl", "rb"))
classes = pickle.load(open("./functions/classes.pkl", "rb"))
lemmatizer = WordNetLemmatizer()

with open("./data/data.json") as file:
    intents = json.load(file)

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str

# Function to Preprocess User Input


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(
        word.lower()) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence, words):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence, words)
    res = model.predict(np.array([bow]))[0]
    return classes[np.argmax(res)]


def get_response(intent_tag):
    for intent in intents["intents"]:
        if intent["tag"] == intent_tag:
            return random.choice(intent["responses"])


@app.get('/')
async def init():
    return "hello shri"


@app.post("/chat/")
async def chat(request: ChatRequest):
    intent = predict_class(request.message)
    now = dt.now()
    response = get_response(intent)
    return {"data": {
        "bot": {
            "message": response,
            "createdAt": now,
            "status": "delivered"
        }
    }}


st.title("Chatbot")
user_input = st.text_input("Enter your message:")
if st.button("Send"):
    response = requests.post(
        "https://vj-pf-chatbot.streamlit.app/chat/", json={"message": user_input})
    st.write("Bot:", response.json()["data"]["bot"]["message"])
