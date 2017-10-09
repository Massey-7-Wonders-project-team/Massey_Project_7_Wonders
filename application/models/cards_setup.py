from .card import Card
from .user import User
from ..controllers.card_logic import db_committing_function
from .wonder import Wonder
import json


def deserialise(serialised_card):
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

def db_populate(app, db):
    ai = []
    for i in range(6):
        name = 'Computer Player ' + str(i+1)
        ai.append(User(
            email=i,
            name=name,
            password=name+str(i)
        ))
    db_committing_function(ai)
    
    with open('application/models/card_data.txt', 'r') as f:
        json_cards = f.readlines()

    with app.app_context():
        for card_string in json_cards:
            card_dict = json.loads(card_string)
            db.session.add(deserialise(card_dict))
        db.session.commit()
    
    #########################################
    ####            WONDERS              ####
    #########################################
    giza_0 = Card(name='giza_0', noPlayers=0, age=0, colour='wonder')
    giza_0.set_benefit_stone(1)
    giza_1 = Card(name='giza_1', noPlayers=0, age=0, colour='wonder')
    giza_1.set_cost_wood(2)
    giza_1.set_benefit_points(3)
    giza_2 = Card(name='giza_2', noPlayers=0, age=0, colour='wonder')
    giza_2.set_cost_stone(3)
    giza_2.set_benefit_points(5)
    giza_3 = Card(name='giza_3', noPlayers=0, age=0, colour='wonder')
    giza_3.set_cost_brick(3)
    giza_3.set_benefit_points(5)
    giza_4 = Card(name='giza_4', noPlayers=0, age=0, colour='wonder')
    giza_4.set_cost_stone(4)
    giza_4.set_cost_paper(1)
    giza_4.set_benefit_points(7)
    giza = Wonder(name="The Pyramids of Giza", slots=4, card_0="giza_0", card_1="giza_1", card_2="giza_2",
                  card_3="giza_3", card_4="giza_4")
    db.session.add_all([giza_0, giza_1, giza_2, giza_3, giza_4, giza])

    alex_0 = Card(name='alex_0', noPlayers=0, age=0, colour='wonder')
    alex_0.set_benefit_glass(1)
    alex_1 = Card(name='alex_1', noPlayers=0, age=0, colour='wonder')
    alex_1.set_cost_brick(2)
    alex_1.set_benefit_brick(1)
    alex_1.set_benefit_ore(1)
    alex_1.set_benefit_stone(1)
    alex_1.set_benefit_wood(1)
    alex_1.set_resource_alternating(True)
    alex_2 = Card(name='alex_2', noPlayers=0, age=0, colour='wonder')
    alex_2.set_cost_wood(2)
    alex_2.set_benefit_glass(1)
    alex_2.set_benefit_paper(1)
    alex_2.set_benefit_cloth(1)
    alex_2.set_resource_alternating(True)
    alex_3 = Card(name='alex_3', noPlayers=0, age=0, colour='wonder')
    alex_3.set_cost_stone(3)
    alex_3.set_benefit_points(7)
    alex = Wonder(name="The Lighthouse of Alexandria", slots=3, card_0="alex_0", card_1="alex_1", card_2="alex_2",
                  card_3="alex_3")
    db.session.add_all([alex_0, alex_1, alex_2, alex_3, alex])

    zeus_0 = Card(name='zeus_0', noPlayers=0, age=0, colour='wonder')
    zeus_0.set_benefit_wood(1)
    zeus_1 = Card(name='zeus_1', noPlayers=0, age=0, colour='wonder')
    zeus_1.set_cost_wood(2)
    zeus_2 = Card(name='zeus_2', noPlayers=0, age=0, colour='wonder')
    zeus_2.set_cost_stone(2)
    zeus_2.set_benefit_points(5)
    zeus_3 = Card(name='zeus_3', noPlayers=0, age=0, colour='wonder')
    zeus_3.set_cost_cloth(1)
    zeus_3.set_cost_ore(2)
    zeus = Wonder(name="The Statue of Zeus in Olympia", slots=3, card_0="zeus_0", card_1="zeus_1", card_2="zeus_2",
                  card_3="zeus_3")
    db.session.add_all([zeus_0, zeus_1, zeus_2, zeus_3, zeus])

    ephesus_0 = Card(name='ephesus_0', noPlayers=0, age=0, colour='wonder')
    ephesus_0.set_benefit_paper(1)
    ephesus_1 = Card(name='ephesus_1', noPlayers=0, age=0, colour='wonder')
    ephesus_1.set_cost_stone(2)
    ephesus_1.set_benefit_points(2)
    ephesus_1.set_benefit_money(4)
    ephesus_2 = Card(name='ephesus_2', noPlayers=0, age=0, colour='wonder')
    ephesus_2.set_cost_wood(2)
    ephesus_2.set_benefit_points(3)
    ephesus_2.set_benefit_money(4)
    ephesus_3 = Card(name='ephesus_3', noPlayers=0, age=0, colour='wonder')
    ephesus_3.set_cost_paper(1)
    ephesus_3.set_cost_cloth(1)
    ephesus_3.set_cost_glass(1)
    ephesus_3.set_benefit_points(5)
    ephesus_3.set_benefit_money(4)
    ephesus = Wonder(name="The Temple of Artemis in Ephesus", slots=3, card_0="ephesus_0", card_1="ephesus_1",
                     card_2="ephesus_2", card_3="ephesus_3")
    db.session.add_all([ephesus_0, ephesus_1, ephesus_2, ephesus_3, ephesus])

    hali_0 = Card(name='hali_0', noPlayers=0, age=0, colour='wonder')
    hali_0.set_benefit_cloth(1)
    hali_1 = Card(name='hali_1', noPlayers=0, age=0, colour='wonder')
    hali_1.set_cost_ore(2)
    hali_1.set_benefit_points(2)
    hali_2 = Card(name='hali_2', noPlayers=0, age=0, colour='wonder')
    hali_2.set_cost_brick(3)
    hali_2.set_benefit_points(1)
    hali_3 = Card(name='hali_3', noPlayers=0, age=0, colour='wonder')
    hali_3.set_cost_cloth(1)
    hali_3.set_cost_paper(1)
    hali_3.set_cost_glass(1)
    hali = Wonder(name="The Mausoleum of Halicarnassus", slots=3, card_0="hali_0", card_1="hali_1", card_2="hali_2",
                  card_3="hali_3")
    db.session.add_all([hali_0, hali_1, hali_2, hali_3, hali])

    rhodes_0 = Card(name='rhodes_0', noPlayers=0, age=0, colour='wonder')
    rhodes_0.set_benefit_ore(1)
    rhodes_1 = Card(name='rhodes_1', noPlayers=0, age=0, colour='wonder')
    rhodes_1.set_cost_stone(3)
    rhodes_1.set_benefit_military(1)
    rhodes_1.set_benefit_money(3)
    rhodes_1.set_benefit_points(3)
    rhodes_2 = Card(name='rhodes_2', noPlayers=0, age=0, colour='wonder')
    rhodes_2.set_cost_ore(4)
    rhodes_2.set_benefit_military(1)
    rhodes_2.set_benefit_money(4)
    rhodes_2.set_benefit_points(4)
    rhodes = Wonder(name="The Colossus of Rhodes", slots=2, card_0="rhodes_0", card_1="rhodes_1", card_2="rhodes_2")
    db.session.add_all([rhodes_0, rhodes_1, rhodes_2, rhodes])

    babylon_0 = Card(name='babylon_0', noPlayers=0, age=0, colour='wonder')
    babylon_0.set_benefit_brick(1)
    babylon_1 = Card(name='babylon_1', noPlayers=0, age=0, colour='wonder')
    babylon_1.set_cost_brick(1)
    babylon_1.set_cost_cloth(1)
    babylon_1.set_benefit_points(3)
    babylon_2 = Card(name='babylon_2', noPlayers=0, age=0, colour='wonder')
    babylon_2.set_cost_glass(1)
    babylon_2.set_cost_wood(2)
    babylon_3 = Card(name='babylon_3', noPlayers=0, age=0, colour='wonder')
    babylon_3.set_cost_paper(1)
    babylon_3.set_cost_brick(3)
    babylon = Wonder(name="The Hanging Gardens of Babylon", slots=3, card_0="babylon_0", card_1="babylon_1",
                     card_2="babylon_2", card_3="babylon_3")
    db.session.add_all([babylon_0, babylon_1, babylon_2, babylon_3, babylon])
    
    with app.app_context():
        db.session.commit()
