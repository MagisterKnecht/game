from random import randrange
import fastapi
import jsonlines

def starting_scenario_generation():

    #this is a method within a larger class
    ### I'm looking for the ability to receive a request from the Node server and return a scenario that can be 
    ### ingested by the game engine. Pass back back info on items + location to begin with

    random_seed = randrange(0,3)
    scenario_files = ['./input_variables/armor_types.jsonl','./input_variables/maps.jsonl']
    
    
    starting_scenario = {
        "map":None,
        "items":None,
        "npcs":None
    }
    
    for input in scenario_files:
        with jsonlines.open(input) as reader:
            print("it got to here")
            armor_types = []
            for choice in reader:
                armor_types.append(choice)
            starting_scenario['armor_type'] = armor_types[random_seed]

    return starting_scenario

# def class match_generator(self, username, time_for_randomness):
#     random_seed = time_for_randomness

#     #distribute players and groups across map

#     #determine locations of items

#     #pick map based on random seed