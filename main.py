from random import randrange
import json
import fastapi

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/random_armor")
async def get_random_armor(armor_class,armor_piece):
    with open('game_data/items.json') as f:
        items = json.load(f)
        armor_components = items['armor_components'][armor_class]
        armor_pieces = items['armor_pieces'][armor_piece]
        random_armor = {
            "armor_component": armor_components[randrange(0,len(armor_components))],
            "armor_piece": armor_pieces[randrange(0,len(armor_pieces))]
        }
        return random_armor