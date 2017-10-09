from .card import Card
from .user import User
from ..controllers.card_logic import db_committing_function
from .wonder import Wonder
import json


def deserialise_card(serialised_card):
    # takes a serialised_card and returns a Card object with the same attributes (except ID)
    deserialised_card = Card(serialised_card['name'], serialised_card['noPlayers'], serialised_card['age'], serialised_card['colour'])
    deserialised_card.costMoney = serialised_card['costMoney']
    deserialised_card.costWood = serialised_card['costWood']
    deserialised_card.costBrick = serialised_card['costBrick']
    deserialised_card.costOre = serialised_card['costOre']
    deserialised_card.costStone = serialised_card['costStone']
    deserialised_card.costGlass = serialised_card['costGlass']
    deserialised_card.costPaper = serialised_card['costPaper']
    deserialised_card.costCloth = serialised_card['costCloth']
    deserialised_card.prerequisite1 = serialised_card['prerequisite1']
    deserialised_card.prerequisite2 = serialised_card['prerequisite2']
    deserialised_card.giveWood = serialised_card['giveWood']
    deserialised_card.giveBrick = serialised_card['giveBrick']
    deserialised_card.giveOre = serialised_card['giveOre']
    deserialised_card.giveStone = serialised_card['giveStone']
    deserialised_card.giveGlass = serialised_card['giveGlass']
    deserialised_card.givePaper = serialised_card['givePaper']
    deserialised_card.giveCloth = serialised_card['giveCloth']
    deserialised_card.resourceAlternating = serialised_card['resourceAlternating']
    deserialised_card.givePoints = serialised_card['givePoints']
    deserialised_card.giveMilitary = serialised_card['giveMilitary']
    deserialised_card.giveMoney = serialised_card['giveMoney']
    deserialised_card.giveResearch = serialised_card['giveResearch']
    return deserialised_card
    
def deserialise_wonder(serialised_wonder):
    # takes a serialised_wonder and returns a Wonder object with the same attributes (except ID)
    return Wonder(name=serialised_wonder['name'], slots=serialised_wonder['slots'], card_0=serialised_wonder['card_0'], card_1=serialised_wonder['card_1'], card_2=serialised_wonder['card_2'], card_3=serialised_wonder['card_3'], card_4=serialised_wonder['card_4'])

def db_populate(app, db):
    #ai
    ai = []
    for i in range(6):
        name = 'Computer Player ' + str(i+1)
        ai.append(User(
            email=i,
            name=name,
            password=name+str(i)
        ))
    db_committing_function(ai)
    
    #cards
    with open('application/models/card_data.txt', 'r') as f:
        json_cards = f.readlines()

    with app.app_context():
        for card_string in json_cards:
            card_dict = json.loads(card_string)
            db.session.add(deserialise_card(card_dict))
        db.session.commit()
    
    #wonders
    with open('application/models/wonder_data.txt', 'r') as f:
        json_wonders = f.readlines()

    with app.app_context():
        for wonder_json in json_wonders:
            wonder_list = json.loads(wonder_json)
            for i in range(len(wonder_list)-1):
                wonder_list[i] = deserialise_card(wonder_list[i])
            wonder_list[-1] = deserialise_wonder(wonder_list[-1])
            for item in wonder_list:
                db.session.add(item)
            
        db.session.commit()
