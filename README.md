#start Virtual ENV
    cmd venv .\venv\Scripts\activate


#start Fast API App
    cmd uvicorn app:app --reload

#Train Chatbot data using JSON
    run file chatbot_training.py 