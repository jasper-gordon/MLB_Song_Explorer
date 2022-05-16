# main.py

from fastapi import FastAPI
import json

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = [


    "http://localhost:5000",

]


app.add_middleware(

    CORSMiddleware,

    allow_origins=origins,

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)


@app.get("/")
async def main():
    return {"message": "Hello World"}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/player_data")
async def get_player_data():
    test_dict = {"arod": "rodria"}
    return test_dict

@app.get('/player_names')
async def get_player_names():
    with open('../players.json') as file:
        player_dict = json.load(file)
    names = list(player_dict.keys())
    names2 = ["hello", "hey there"]
    return names
