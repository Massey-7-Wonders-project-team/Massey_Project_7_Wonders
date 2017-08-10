from .card import Card

def db_load_test_cards(app, db):
    #tavern = Card('Tavern', 4, 1, 'yellow')
    #tavern.add_benefit_money(5)
    cardList = []
    
    lumberYard = Card('Lumber Yard', 3, 1, 'brown')
    lumberYard.add_benefit_wood(1)
    cardList.append(lumberYard)
    
    oreVein = Card('Ore Vein', 3, 1, 'brown')
    oreVein.add_benefit_ore(1)
    cardList.append(oreVein)
    
    clayPool = Card('Clay Pool', 3, 1, 'brown')
    clayPool.add_benefit_brick(1)
    cardList.append(clayPool)
    
    stonePit = Card('Stone Pit', 3, 1, 'brown')
    stonePit.add_benefit_stone(1)
    cardList.append(stonePit)
    
    timberYard = Card('Timber Yard', 3, 1, 'brown')
    timberYard.add_benefit_wood(1)
    timberYard.add_benefit_stone(1)
    timberYard.set_resource_alternating(True)
    cardList.append(timberYard)
    
    clayPit = Card('Clay Pit', 3, 1, 'brown')
    clayPit.add_benefit_brick(1)
    clayPit.add_benefit_ore(1)
    clayPit.set_resource_alternating(True)
    cardList.append(clayPit)
    
    loom = Card('Loom', 3, 1, 'grey')
    loom.add_benefit_cloth(1)
    cardList.append(loom)
    
    glassworks = Card('Glassworks', 3, 1, 'grey')
    glassworks.add_benefit_glass(1)
    cardList.append(glassworks)
    
    press = Card('Press', 3, 1, 'grey')
    press.add_benefit_paper(1)
    cardList.append(press)
    
    eastTradingPost = Card('East Trading Post', 3, 1, 'yellow')
    cardList.append(eastTradingPost)
    
    westTradingPost = Card('West Trading Post', 3, 1, 'yellow')
    cardList.append(westTradingPost)
    
    marketplace = Card('Marketplace', 3, 1, 'yellow')
    cardList.append(marketplace)
    
    altar = Card('Altar', 3, 1, 'blue')
    altar.add_benefit_points(2)
    cardList.append(altar)
    
    theatre = Card('Theatre', 3, 1, 'blue')
    theatre.add_benefit_points(2)
    cardList.append(theatre)
    
    baths = Card('Baths', 3, 1, 'blue')
    baths.add_cost_stone(1)
    baths.add_benefit_points(3)
    cardList.append(baths)
    
    stockade = Card('Stockade', 3, 1, 'red')
    stockade.add_cost_wood(1)
    stockade.add_benefit_military(1)
    cardList.append(stockade)
    
    barracks = Card('Barracks', 3, 1, 'red')
    barracks.add_cost_ore(1)
    barracks.add_benefit_military(1)
    cardList.append(barracks)
    
    guardTower = Card('Guard Tower', 3, 1, 'red')
    guardTower.add_cost_brick(1)
    guardTower.add_benefit_military(1)
    cardList.append(guardTower)
    
    apothecary = Card('Apothecary', 3, 1, 'green')
    apothecary.add_cost_cloth(1)
    apothecary.add_benefit_research('compass')
    cardList.append(apothecary)
    
    workshop = Card('Workshop', 3, 1, 'green')
    workshop.add_cost_glass(1)
    workshop.add_benefit_research('cog')
    cardList.append(workshop)
    
    scriptorium = Card('Scriptorium', 3, 1, 'green')
    scriptorium.add_cost_paper(1)
    scriptorium.add_benefit_research('tablet')
    cardList.append(scriptorium)
    
    with app.app_context():
        for card in cardList:
            db.session.add(card)
        db.session.commit()
