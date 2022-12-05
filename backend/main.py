import os
import json
import time
import logging
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from playwright.sync_api import sync_playwright


app = FastAPI()

# playwright
play = sync_playwright().start()
browser = play.chromium.launch_persistent_context(
    user_data_dir="/tmp/playwright",
    headless=False,
)
page = browser.new_page()


origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

headers = {
    "Content-Type": "application/json"
}


@app.get("/")
def root():
    return {"message": "welcome to af"}


@app.get("/chat")
def chat():
    return ""
