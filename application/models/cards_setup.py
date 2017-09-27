from .card import Card
from .user import User
from ..controllers.card_logic import db_committing_function
from .wonder import Wonder


def db_populate_cards(app, db):
    #########################################
    ####~~~~~~~~~Computer Users~~~~~~~~~~####
    #########################################
    ai = []
    for i in range(6):
        name = 'Computer Player ' + str(i + 1)
        ai.append(User(
            email=i,
            name=name,
            password=name + str(i)
        ))
    db_committing_function(ai)

    cardList = []
    #########################################
    ####~~~~~~~~~~~~~~Age 1~~~~~~~~~~~~~~####
    #########################################

    # ~~~3 Player~~~#

    lumberYard = Card('Lumber Yard', 3, 1, 'brown')
    lumberYard.set_benefit_wood(1)
    cardList.append(lumberYard)

    oreVein = Card('Ore Vein', 3, 1, 'brown')
    oreVein.set_benefit_ore(1)
    cardList.append(oreVein)

    clayPool = Card('Clay Pool', 3, 1, 'brown')
    clayPool.set_benefit_brick(1)
    cardList.append(clayPool)

    stonePit = Card('Stone Pit', 3, 1, 'brown')
    stonePit.set_benefit_stone(1)
    cardList.append(stonePit)

    timberYard = Card('Timber Yard', 3, 1, 'brown')
    timberYard.set_benefit_wood(1)
    timberYard.set_benefit_stone(1)
    timberYard.set_resource_alternating(True)
    timberYard.set_cost_money(1)
    cardList.append(timberYard)

    clayPit = Card('Clay Pit', 3, 1, 'brown')
    clayPit.set_benefit_brick(1)
    clayPit.set_benefit_ore(1)
    clayPit.set_resource_alternating(True)
    clayPit.set_cost_money(1)
    cardList.append(clayPit)

    loom = Card('Loom', 3, 1, 'grey')
    loom.set_benefit_cloth(1)
    cardList.append(loom)

    glassworks = Card('Glassworks', 3, 1, 'grey')
    glassworks.set_benefit_glass(1)
    cardList.append(glassworks)

    press = Card('Press', 3, 1, 'grey')
    press.set_benefit_paper(1)
    cardList.append(press)

    eastTradingPost = Card('East Trading Post', 3, 1, 'yellow')
    cardList.append(eastTradingPost)

    westTradingPost = Card('West Trading Post', 3, 1, 'yellow')
    cardList.append(westTradingPost)

    marketplace = Card('Marketplace', 3, 1, 'yellow')
    cardList.append(marketplace)

    altar = Card('Altar', 3, 1, 'blue')
    altar.set_benefit_points(2)
    cardList.append(altar)

    theatre = Card('Theatre', 3, 1, 'blue')
    theatre.set_benefit_points(2)
    cardList.append(theatre)

    baths = Card('Baths', 3, 1, 'blue')
    baths.set_cost_stone(1)
    baths.set_benefit_points(3)
    cardList.append(baths)

    stockade = Card('Stockade', 3, 1, 'red')
    stockade.set_cost_wood(1)
    stockade.set_benefit_military(1)
    cardList.append(stockade)

    barracks = Card('Barracks', 3, 1, 'red')
    barracks.set_cost_ore(1)
    barracks.set_benefit_military(1)
    cardList.append(barracks)

    guardTower = Card('Guard Tower', 3, 1, 'red')
    guardTower.set_cost_brick(1)
    guardTower.set_benefit_military(1)
    cardList.append(guardTower)

    apothecary = Card('Apothecary', 3, 1, 'green')
    apothecary.set_cost_cloth(1)
    apothecary.set_benefit_research('compass')
    cardList.append(apothecary)

    workshop = Card('Workshop', 3, 1, 'green')
    workshop.set_cost_glass(1)
    workshop.set_benefit_research('cog')
    cardList.append(workshop)

    scriptorium = Card('Scriptorium', 3, 1, 'green')
    scriptorium.set_cost_paper(1)
    scriptorium.set_benefit_research('tablet')
    cardList.append(scriptorium)

    # ~~~4 Player~~~#

    lumberYard = Card('Lumber Yard', 4, 1, 'brown')
    lumberYard.set_benefit_wood(1)
    cardList.append(lumberYard)

    oreVein = Card('Ore Vein', 4, 1, 'brown')
    oreVein.set_benefit_ore(1)
    cardList.append(oreVein)

    excavation = Card('Excavation', 4, 1, 'brown')
    excavation.set_benefit_stone(1)
    excavation.set_benefit_brick(1)
    excavation.set_resource_alternating(True)
    excavation.set_cost_money(1)
    cardList.append(excavation)

    pawnshop = Card('Pawnshop', 4, 1, 'blue')
    pawnshop.set_benefit_points(3)
    cardList.append(pawnshop)

    tavern = Card('Tavern', 4, 1, 'yellow')
    tavern.set_benefit_money(5)
    cardList.append(tavern)

    guardTower = Card('Guard Tower', 4, 1, 'red')
    guardTower.set_cost_brick(1)
    guardTower.set_benefit_military(1)
    cardList.append(guardTower)

    scriptorium = Card('Scriptorium', 4, 1, 'green')
    scriptorium.set_cost_paper(1)
    scriptorium.set_benefit_research('tablet')
    cardList.append(scriptorium)

    # ~~~5 Player~~~#

    stonePit = Card('Stone Pit', 5, 1, 'brown')
    stonePit.set_benefit_stone(1)
    cardList.append(stonePit)

    clayPool = Card('Clay Pool', 5, 1, 'brown')
    clayPool.set_benefit_brick(1)
    cardList.append(clayPool)

    forestCave = Card('Forest Cave', 5, 1, 'brown')
    forestCave.set_benefit_wood(1)
    forestCave.set_benefit_ore(1)
    forestCave.set_resource_alternating(True)
    forestCave.set_cost_money(1)
    cardList.append(forestCave)

    altar = Card('Altar', 5, 1, 'blue')
    altar.set_benefit_points(2)
    cardList.append(altar)

    tavern = Card('Tavern', 5, 1, 'yellow')
    tavern.set_benefit_money(5)
    cardList.append(tavern)

    barracks = Card('Barracks', 5, 1, 'red')
    barracks.set_cost_ore(1)
    barracks.set_benefit_military(1)
    cardList.append(barracks)

    apothecary = Card('Apothecary', 5, 1, 'green')
    apothecary.set_cost_cloth(1)
    apothecary.set_benefit_research('compass')
    cardList.append(apothecary)

    # ~~~6 Player~~~#

    treeFarm = Card('Tree Farm', 6, 1, 'brown')
    treeFarm.set_benefit_wood(1)
    treeFarm.set_benefit_brick(1)
    treeFarm.set_resource_alternating(True)
    treeFarm.set_cost_money(1)
    cardList.append(treeFarm)

    mine = Card('Mine', 6, 1, 'brown')
    mine.set_benefit_stone(1)
    mine.set_benefit_ore(1)
    mine.set_resource_alternating(True)
    mine.set_cost_money(1)
    cardList.append(mine)

    loom = Card('Loom', 6, 1, 'grey')
    loom.set_benefit_cloth(1)
    cardList.append(loom)

    glassworks = Card('Glassworks', 6, 1, 'grey')
    glassworks.set_benefit_glass(1)
    cardList.append(glassworks)

    press = Card('Press', 6, 1, 'grey')
    press.set_benefit_paper(1)
    cardList.append(press)

    theatre = Card('Theatre', 6, 1, 'blue')
    theatre.set_benefit_points(2)
    cardList.append(theatre)

    marketplace = Card('Marketplace', 6, 1, 'yellow')
    cardList.append(marketplace)

    # ~~~7 Player~~~#

    pawnshop = Card('Pawnshop', 7, 1, 'blue')
    pawnshop.set_benefit_points(3)
    cardList.append(pawnshop)

    baths = Card('Baths', 7, 1, 'blue')
    baths.set_cost_stone(1)
    baths.set_benefit_points(3)
    cardList.append(baths)

    tavern = Card('Tavern', 7, 1, 'yellow')
    tavern.set_benefit_money(5)
    cardList.append(tavern)

    eastTradingPost = Card('East Trading Post', 7, 1, 'yellow')
    cardList.append(eastTradingPost)

    westTradingPost = Card('West Trading Post', 7, 1, 'yellow')
    cardList.append(westTradingPost)

    stockade = Card('Stockade', 7, 1, 'red')
    stockade.set_cost_wood(1)
    stockade.set_benefit_military(1)
    cardList.append(stockade)

    workshop = Card('Workshop', 7, 1, 'green')
    workshop.set_cost_glass(1)
    workshop.set_benefit_research('cog')
    cardList.append(workshop)

    #########################################
    ####~~~~~~~~~~~~~~Age 1~~~~~~~~~~~~~~####
    #########################################

    # ~~~3 Player~~~#

    sawmill = Card('Sawmill', 3, 2, 'brown')
    sawmill.set_benefit_wood(2)
    sawmill.set_cost_money(1)
    cardList.append(sawmill)

    foundry = Card('Foundry', 3, 2, 'brown')
    foundry.set_benefit_ore(2)
    foundry.set_cost_money(1)
    cardList.append(foundry)

    brickYard = Card('Brick Yard', 3, 2, 'brown')
    brickYard.set_benefit_brick(2)
    brickYard.set_cost_money(1)
    cardList.append(brickYard)

    quarry = Card('Quarry', 3, 2, 'brown')
    quarry.set_benefit_stone(2)
    quarry.set_cost_money(1)
    cardList.append(quarry)

    loom = Card('Loom', 3, 2, 'grey')
    loom.set_benefit_cloth(1)
    cardList.append(loom)

    glassworks = Card('Glassworks', 3, 2, 'grey')
    glassworks.set_benefit_glass(1)
    cardList.append(glassworks)

    press = Card('Press', 3, 2, 'grey')
    press.set_benefit_paper(1)
    cardList.append(press)

    caravansery = Card('Caravansery', 3, 2, 'yellow')
    caravansery.set_benefit_wood(1)
    caravansery.set_benefit_ore(1)
    caravansery.set_benefit_brick(1)
    caravansery.set_benefit_stone(1)
    caravansery.set_resource_alternating(True)
    caravansery.set_cost_wood(2)
    caravansery.set_prerequisite_1('Marketplace')
    cardList.append(caravansery)

    forum = Card('Forum', 3, 2, 'yellow')
    forum.set_benefit_cloth(1)
    forum.set_benefit_glass(1)
    forum.set_benefit_paper(1)
    forum.set_resource_alternating(True)
    forum.set_cost_brick(2)
    forum.set_prerequisite_1('East Trading Post')
    forum.set_prerequisite_2('West Trading Post')
    cardList.append(forum)

    vineyard = Card('Vineyard', 3, 2, 'yellow')
    cardList.append(vineyard)

    temple = Card('Temple', 3, 2, 'blue')
    temple.set_benefit_points(3)
    temple.set_cost_wood(1)
    temple.set_cost_brick(1)
    temple.set_cost_glass(1)
    temple.set_prerequisite_1('Altar')
    cardList.append(temple)

    courthouse = Card('Courthouse', 3, 2, 'blue')
    courthouse.set_benefit_points(4)
    courthouse.set_cost_brick(2)
    courthouse.set_cost_cloth(1)
    courthouse.set_prerequisite_1('Scriptorium')
    cardList.append(courthouse)

    statue = Card('Statue', 3, 2, 'blue')
    statue.set_benefit_points(4)
    statue.set_cost_ore(2)
    statue.set_cost_wood(1)
    statue.set_prerequisite_1('Theatre')
    cardList.append(statue)

    aqueduct = Card('Aqueduct', 3, 2, 'blue')
    aqueduct.set_benefit_points(5)
    aqueduct.set_cost_stone(3)
    aqueduct.set_prerequisite_1('Baths')
    cardList.append(aqueduct)

    stables = Card('Stables', 3, 2, 'red')
    stables.set_benefit_military(2)
    stables.set_cost_brick(1)
    stables.set_cost_wood(1)
    stables.set_cost_ore(1)
    stables.set_prerequisite_1('Apothecary')
    cardList.append(stables)

    archeryRange = Card('Archery Range', 3, 2, 'red')
    archeryRange.set_benefit_military(2)
    archeryRange.set_cost_wood(2)
    archeryRange.set_cost_ore(1)
    archeryRange.set_prerequisite_1('Workshop')
    cardList.append(archeryRange)

    walls = Card('Walls', 3, 2, 'red')
    walls.set_benefit_military(2)
    walls.set_cost_stone(3)
    cardList.append(walls)

    library = Card('Library', 3, 2, 'green')
    library.set_benefit_research('tablet')
    library.set_cost_stone(2)
    library.set_cost_cloth(1)
    library.set_prerequisite_1('Scriptorium')
    cardList.append(library)

    laboratory = Card('Laboratory', 3, 2, 'green')
    laboratory.set_benefit_research('cog')
    laboratory.set_cost_brick(2)
    laboratory.set_cost_paper(1)
    laboratory.set_prerequisite_1('Workshop')
    cardList.append(laboratory)

    dispensary = Card('Dispensary', 3, 2, 'green')
    dispensary.set_benefit_research('compass')
    dispensary.set_cost_ore(2)
    dispensary.set_cost_glass(1)
    dispensary.set_prerequisite_1('Apothecary')
    cardList.append(dispensary)

    school = Card('School', 3, 2, 'green')
    school.set_benefit_research('tablet')
    school.set_cost_wood(1)
    school.set_cost_paper(1)
    cardList.append(school)

    # ~~~4 Player~~~#

    sawmill = Card('Sawmill', 4, 2, 'brown')
    sawmill.set_benefit_wood(2)
    sawmill.set_cost_money(1)
    cardList.append(sawmill)

    foundry = Card('Foundry', 4, 2, 'brown')
    foundry.set_benefit_ore(2)
    foundry.set_cost_money(1)
    cardList.append(foundry)

    brickYard = Card('Brick Yard', 4, 2, 'brown')
    brickYard.set_benefit_brick(2)
    brickYard.set_cost_money(1)
    cardList.append(brickYard)

    quarry = Card('Quarry', 4, 2, 'brown')
    quarry.set_benefit_stone(2)
    quarry.set_cost_money(1)
    cardList.append(quarry)

    bazaar = Card('Bazaar', 4, 2, 'yellow')
    cardList.append(bazaar)

    trainingGround = Card('Training Ground', 4, 2, 'red')
    trainingGround.set_benefit_military(2)
    trainingGround.set_cost_ore(2)
    trainingGround.set_cost_wood(1)
    cardList.append(trainingGround)

    dispensary = Card('Dispensary', 4, 2, 'green')
    dispensary.set_benefit_research('compass')
    dispensary.set_cost_ore(2)
    dispensary.set_cost_glass(1)
    dispensary.set_prerequisite_1('Apothecary')
    cardList.append(dispensary)

    # ~~~5 Player~~~#

    loom = Card('Loom', 5, 2, 'grey')
    loom.set_benefit_cloth(1)
    cardList.append(loom)

    glassworks = Card('Glassworks', 5, 2, 'grey')
    glassworks.set_benefit_glass(1)
    cardList.append(glassworks)

    press = Card('Press', 5, 2, 'grey')
    press.set_benefit_paper(1)
    cardList.append(press)

    courthouse = Card('Courthouse', 5, 2, 'blue')
    courthouse.set_benefit_points(4)
    courthouse.set_cost_brick(2)
    courthouse.set_cost_cloth(1)
    courthouse.set_prerequisite_1('Scriptorium')
    cardList.append(courthouse)

    caravansery = Card('Caravansery', 5, 2, 'yellow')
    caravansery.set_benefit_wood(1)
    caravansery.set_benefit_ore(1)
    caravansery.set_benefit_brick(1)
    caravansery.set_benefit_stone(1)
    caravansery.set_resource_alternating(True)
    caravansery.set_cost_wood(2)
    caravansery.set_prerequisite_1('Marketplace')
    cardList.append(caravansery)

    stables = Card('Stables', 5, 2, 'red')
    stables.set_benefit_military(2)
    stables.set_cost_brick(1)
    stables.set_cost_wood(1)
    stables.set_cost_ore(1)
    stables.set_prerequisite_1('Apothecary')
    cardList.append(stables)

    laboratory = Card('Laboratory', 5, 2, 'green')
    laboratory.set_benefit_research('cog')
    laboratory.set_cost_brick(2)
    laboratory.set_cost_paper(1)
    laboratory.set_prerequisite_1('Workshop')
    cardList.append(laboratory)

    # ~~~6 Player~~~#

    temple = Card('Temple', 6, 2, 'blue')
    temple.set_benefit_points(3)
    temple.set_cost_wood(1)
    temple.set_cost_brick(1)
    temple.set_cost_glass(1)
    temple.set_prerequisite_1('Altar')
    cardList.append(temple)

    forum = Card('Forum', 6, 2, 'yellow')
    forum.set_benefit_cloth(1)
    forum.set_benefit_glass(1)
    forum.set_benefit_paper(1)
    forum.set_resource_alternating(True)
    forum.set_cost_brick(2)
    forum.set_prerequisite_1('East Trading Post')
    forum.set_prerequisite_2('West Trading Post')
    cardList.append(forum)

    caravansery = Card('Caravansery', 6, 2, 'yellow')
    caravansery.set_benefit_wood(1)
    caravansery.set_benefit_ore(1)
    caravansery.set_benefit_brick(1)
    caravansery.set_benefit_stone(1)
    caravansery.set_resource_alternating(True)
    caravansery.set_cost_wood(2)
    caravansery.set_prerequisite_1('Marketplace')
    cardList.append(caravansery)

    vineyard = Card('Vineyard', 6, 2, 'yellow')
    cardList.append(vineyard)

    trainingGround = Card('Training Ground', 6, 2, 'red')
    trainingGround.set_benefit_military(2)
    trainingGround.set_cost_ore(2)
    trainingGround.set_cost_wood(1)
    cardList.append(trainingGround)

    archeryRange = Card('Archery Range', 6, 2, 'red')
    archeryRange.set_benefit_military(2)
    archeryRange.set_cost_wood(2)
    archeryRange.set_cost_ore(1)
    archeryRange.set_prerequisite_1('Workshop')
    cardList.append(archeryRange)

    library = Card('Library', 6, 2, 'green')
    library.set_benefit_research('tablet')
    library.set_cost_stone(2)
    library.set_cost_cloth(1)
    library.set_prerequisite_1('Scriptorium')
    cardList.append(library)

    # ~~~7 Player~~~#

    aqueduct = Card('Aqueduct', 7, 2, 'blue')
    aqueduct.set_benefit_points(5)
    aqueduct.set_cost_stone(3)
    aqueduct.set_prerequisite_1('Baths')
    cardList.append(aqueduct)

    statue = Card('Statue', 7, 2, 'blue')
    statue.set_benefit_points(4)
    statue.set_cost_ore(2)
    statue.set_cost_wood(1)
    statue.set_prerequisite_1('Theatre')
    cardList.append(statue)

    forum = Card('Forum', 7, 2, 'yellow')
    forum.set_benefit_cloth(1)
    forum.set_benefit_glass(1)
    forum.set_benefit_paper(1)
    forum.set_resource_alternating(True)
    forum.set_cost_brick(2)
    forum.set_prerequisite_1('East Trading Post')
    forum.set_prerequisite_2('West Trading Post')
    cardList.append(forum)

    bazaar = Card('Bazaar', 7, 2, 'yellow')
    cardList.append(bazaar)

    walls = Card('Walls', 7, 2, 'red')
    walls.set_benefit_military(2)
    walls.set_cost_stone(3)
    cardList.append(walls)

    trainingGround = Card('Training Ground', 7, 2, 'red')
    trainingGround.set_benefit_military(2)
    trainingGround.set_cost_ore(2)
    trainingGround.set_cost_wood(1)
    cardList.append(trainingGround)

    school = Card('School', 7, 2, 'green')
    school.set_benefit_research('tablet')
    school.set_cost_wood(1)
    school.set_cost_paper(1)
    cardList.append(school)

    #########################################
    ####~~~~~~~~~~~~~~Age 3~~~~~~~~~~~~~~####
    #########################################

    # ~~~3 Player~~~#

    gardens = Card('Gardens', 3, 3, 'blue')
    gardens.set_benefit_points(5)
    gardens.set_cost_brick(2)
    gardens.set_cost_wood(1)
    gardens.set_prerequisite_1('Statue')
    cardList.append(gardens)

    senate = Card('Senate', 3, 3, 'blue')
    senate.set_benefit_points(6)
    senate.set_cost_wood(2)
    senate.set_cost_stone(1)
    senate.set_cost_ore(1)
    senate.set_prerequisite_1('Library')
    cardList.append(senate)

    townHall = Card('Town Hall', 3, 3, 'blue')
    townHall.set_benefit_points(6)
    townHall.set_cost_stone(2)
    townHall.set_cost_ore(1)
    townHall.set_cost_glass(1)
    cardList.append(townHall)

    pantheon = Card('Pantheon', 3, 3, 'blue')
    pantheon.set_benefit_points(7)
    pantheon.set_cost_brick(2)
    pantheon.set_cost_ore(1)
    pantheon.set_cost_glass(1)
    pantheon.set_cost_paper(1)
    pantheon.set_cost_cloth(1)
    pantheon.set_prerequisite_1('Temple')
    cardList.append(pantheon)

    palace = Card('Palace', 3, 3, 'blue')
    palace.set_benefit_points(8)
    palace.set_cost_stone(1)
    palace.set_cost_ore(1)
    palace.set_cost_wood(1)
    palace.set_cost_brick(1)
    palace.set_cost_glass(1)
    palace.set_cost_paper(1)
    palace.set_cost_cloth(1)
    cardList.append(palace)

    university = Card('University', 3, 3, 'green')
    university.set_benefit_research('tablet')
    university.set_cost_wood(2)
    university.set_cost_paper(1)
    university.set_cost_cloth(1)
    university.set_prerequisite_1('Library')
    cardList.append(university)

    observatory = Card('Observatory', 3, 3, 'green')
    observatory.set_benefit_research('cog')
    observatory.set_cost_ore(2)
    observatory.set_cost_glass(1)
    observatory.set_cost_cloth(1)
    observatory.set_prerequisite_1('Laboratory')
    cardList.append(observatory)

    study = Card('Study', 3, 3, 'green')
    study.set_benefit_research('cog')
    study.set_cost_wood(1)
    study.set_cost_paper(1)
    study.set_cost_cloth(1)
    study.set_prerequisite_1('School')
    cardList.append(study)

    lodge = Card('Lodge', 3, 3, 'green')
    lodge.set_benefit_research('compass')
    lodge.set_cost_brick(2)
    lodge.set_cost_paper(1)
    lodge.set_cost_cloth(1)
    lodge.set_prerequisite_1('Dispensary')
    cardList.append(lodge)

    academy = Card('Academy', 3, 3, 'green')
    academy.set_benefit_research('compass')
    academy.set_cost_stone(3)
    academy.set_cost_glass(1)
    academy.set_prerequisite_1('School')
    cardList.append(academy)

    siegeWorkshop = Card('Siege Workshop', 3, 3, 'red')
    siegeWorkshop.set_benefit_military(3)
    siegeWorkshop.set_cost_brick(3)
    siegeWorkshop.set_cost_wood(1)
    siegeWorkshop.set_prerequisite_1('Laboratory')
    cardList.append(siegeWorkshop)

    fortification = Card('Fortification', 3, 3, 'red')
    fortification.set_benefit_military(3)
    fortification.set_cost_ore(3)
    fortification.set_cost_stone(1)
    fortification.set_prerequisite_1('Walls')
    cardList.append(fortification)

    arsenal = Card('Arsenal', 3, 3, 'red')
    arsenal.set_benefit_military(3)
    arsenal.set_cost_wood(2)
    arsenal.set_cost_ore(1)
    arsenal.set_cost_cloth(1)
    cardList.append(arsenal)

    arena = Card('Arena', 3, 3, 'yellow')
    arena.set_cost_stone(2)
    arena.set_cost_ore(1)
    arena.set_prerequisite_1('Dispensary')
    cardList.append(arena)

    lighthouse = Card('Lighthouse', 3, 3, 'yellow')
    lighthouse.set_cost_stone(1)
    lighthouse.set_cost_glass(1)
    lighthouse.set_prerequisite_1('Caravansery')
    cardList.append(lighthouse)

    haven = Card('Haven', 3, 3, 'yellow')
    haven.set_cost_wood(1)
    haven.set_cost_ore(1)
    haven.set_cost_cloth(1)
    haven.set_prerequisite_1('Forum')
    cardList.append(haven)

    # ~~~4 Player~~~#

    gardens = Card('Gardens', 4, 3, 'blue')
    gardens.set_benefit_points(5)
    gardens.set_cost_brick(2)
    gardens.set_cost_wood(1)
    gardens.set_prerequisite_1('Statue')
    cardList.append(gardens)

    haven = Card('Haven', 4, 3, 'yellow')
    haven.set_cost_wood(1)
    haven.set_cost_ore(1)
    haven.set_cost_cloth(1)
    haven.set_prerequisite_1('Forum')
    cardList.append(haven)

    chamberOfCommerce = Card('Chamber Of Commerce', 4, 3, 'yellow')
    chamberOfCommerce.set_cost_brick(2)
    chamberOfCommerce.set_cost_paper(1)
    cardList.append(chamberOfCommerce)

    circus = Card('Circus', 4, 3, 'red')
    circus.set_benefit_military(3)
    circus.set_cost_stone(3)
    circus.set_cost_ore(1)
    circus.set_prerequisite_1('Training Ground')
    cardList.append(circus)

    arsenal = Card('Arsenal', 4, 3, 'red')
    arsenal.set_benefit_military(3)
    arsenal.set_cost_wood(2)
    arsenal.set_cost_ore(1)
    arsenal.set_cost_cloth(1)
    cardList.append(arsenal)

    university = Card('University', 4, 3, 'green')
    university.set_benefit_research('tablet')
    university.set_cost_wood(2)
    university.set_cost_paper(1)
    university.set_cost_cloth(1)
    university.set_prerequisite_1('Library')
    cardList.append(university)

    # ~~~5 Player~~~#

    townHall = Card('Town Hall', 5, 3, 'blue')
    townHall.set_benefit_points(6)
    townHall.set_cost_stone(2)
    townHall.set_cost_ore(1)
    townHall.set_cost_glass(1)
    cardList.append(townHall)

    senate = Card('Senate', 5, 3, 'blue')
    senate.set_benefit_points(6)
    senate.set_cost_wood(2)
    senate.set_cost_stone(1)
    senate.set_cost_ore(1)
    senate.set_prerequisite_1('Library')
    cardList.append(senate)

    arena = Card('Arena', 5, 3, 'yellow')
    arena.set_cost_stone(2)
    arena.set_cost_ore(1)
    arena.set_prerequisite_1('Dispensary')
    cardList.append(arena)

    circus = Card('Circus', 5, 3, 'red')
    circus.set_benefit_military(3)
    circus.set_cost_stone(3)
    circus.set_cost_ore(1)
    circus.set_prerequisite_1('Training Ground')
    cardList.append(circus)

    siegeWorkshop = Card('Siege Workshop', 5, 3, 'red')
    siegeWorkshop.set_benefit_military(3)
    siegeWorkshop.set_cost_brick(3)
    siegeWorkshop.set_cost_wood(1)
    siegeWorkshop.set_prerequisite_1('Laboratory')
    cardList.append(siegeWorkshop)

    study = Card('Study', 5, 3, 'green')
    study.set_benefit_research('cog')
    study.set_cost_wood(1)
    study.set_cost_paper(1)
    study.set_cost_cloth(1)
    study.set_prerequisite_1('School')
    cardList.append(study)

    # ~~~6 Player~~~#

    pantheon = Card('Pantheon', 6, 3, 'blue')
    pantheon.set_benefit_points(7)
    pantheon.set_cost_brick(2)
    pantheon.set_cost_ore(1)
    pantheon.set_cost_glass(1)
    pantheon.set_cost_paper(1)
    pantheon.set_cost_cloth(1)
    pantheon.set_prerequisite_1('Temple')
    cardList.append(pantheon)

    townHall = Card('Town Hall', 6, 3, 'blue')
    townHall.set_benefit_points(6)
    townHall.set_cost_stone(2)
    townHall.set_cost_ore(1)
    townHall.set_cost_glass(1)
    cardList.append(townHall)

    lighthouse = Card('Lighthouse', 6, 3, 'yellow')
    lighthouse.set_cost_stone(1)
    lighthouse.set_cost_glass(1)
    lighthouse.set_prerequisite_1('Caravansery')
    cardList.append(lighthouse)

    chamberOfCommerce = Card('Chamber Of Commerce', 6, 3, 'yellow')
    chamberOfCommerce.set_cost_brick(2)
    chamberOfCommerce.set_cost_paper(1)
    cardList.append(chamberOfCommerce)

    circus = Card('Circus', 6, 3, 'red')
    circus.set_benefit_military(3)
    circus.set_cost_stone(3)
    circus.set_cost_ore(1)
    circus.set_prerequisite_1('Training Ground')
    cardList.append(circus)

    lodge = Card('Lodge', 6, 3, 'green')
    lodge.set_benefit_research('compass')
    lodge.set_cost_brick(2)
    lodge.set_cost_paper(1)
    lodge.set_cost_cloth(1)
    lodge.set_prerequisite_1('Dispensary')
    cardList.append(lodge)

    # ~~~7 Player~~~#

    palace = Card('Palace', 7, 3, 'blue')
    palace.set_benefit_points(8)
    palace.set_cost_stone(1)
    palace.set_cost_ore(1)
    palace.set_cost_wood(1)
    palace.set_cost_brick(1)
    palace.set_cost_glass(1)
    palace.set_cost_paper(1)
    palace.set_cost_cloth(1)
    cardList.append(palace)

    arena = Card('Arena', 7, 3, 'yellow')
    arena.set_cost_stone(2)
    arena.set_cost_ore(1)
    arena.set_prerequisite_1('Dispensary')
    cardList.append(arena)

    fortification = Card('Fortification', 7, 3, 'red')
    fortification.set_benefit_military(3)
    fortification.set_cost_ore(3)
    fortification.set_cost_stone(1)
    fortification.set_prerequisite_1('Walls')
    cardList.append(fortification)

    arsenal = Card('Arsenal', 7, 3, 'red')
    arsenal.set_benefit_military(3)
    arsenal.set_cost_wood(2)
    arsenal.set_cost_ore(1)
    arsenal.set_cost_cloth(1)
    cardList.append(arsenal)

    observatory = Card('Observatory', 7, 3, 'green')
    observatory.set_benefit_research('cog')
    observatory.set_cost_ore(2)
    observatory.set_cost_glass(1)
    observatory.set_cost_cloth(1)
    observatory.set_prerequisite_1('Laboratory')
    cardList.append(observatory)

    academy = Card('Academy', 7, 3, 'green')
    academy.set_benefit_research('compass')
    academy.set_cost_stone(3)
    academy.set_cost_glass(1)
    academy.set_prerequisite_1('School')
    cardList.append(academy)

    # ~~~ Guilds ~~~#

    workersGuild = Card('Workers Guild', 0, 3, 'purple')
    workersGuild.set_cost_ore(2)
    workersGuild.set_cost_brick(1)
    workersGuild.set_cost_stone(1)
    workersGuild.set_cost_wood(1)
    cardList.append(workersGuild)

    craftsmensGuild = Card('Craftsmens Guild', 0, 3, 'purple')
    craftsmensGuild.set_cost_ore(2)
    craftsmensGuild.set_cost_stone(2)
    cardList.append(craftsmensGuild)

    shipownersGuild = Card('Shipowners Guild', 0, 3, 'purple')
    shipownersGuild.set_cost_wood(3)
    shipownersGuild.set_cost_glass(1)
    shipownersGuild.set_cost_paper(1)
    cardList.append(shipownersGuild)

    tradersGuild = Card('Traders Guild', 0, 3, 'purple')
    tradersGuild.set_cost_glass(1)
    tradersGuild.set_cost_cloth(1)
    tradersGuild.set_cost_paper(1)
    cardList.append(tradersGuild)

    magistratesGuild = Card('Magistrates Guild', 0, 3, 'purple')
    magistratesGuild.set_cost_wood(3)
    magistratesGuild.set_cost_stone(1)
    magistratesGuild.set_cost_cloth(1)
    cardList.append(magistratesGuild)

    buildersGuild = Card('Builders Guild', 0, 3, 'purple')
    buildersGuild.set_cost_stone(2)
    buildersGuild.set_cost_brick(2)
    buildersGuild.set_cost_glass(1)
    cardList.append(buildersGuild)

    philosophersGuild = Card('Philosophers Guild', 0, 3, 'purple')
    philosophersGuild.set_cost_brick(3)
    philosophersGuild.set_cost_paper(1)
    philosophersGuild.set_cost_cloth(1)
    cardList.append(philosophersGuild)

    scientistsGuild = Card('Scientists Guild', 0, 3, 'purple')
    scientistsGuild.set_cost_wood(2)
    scientistsGuild.set_cost_ore(2)
    scientistsGuild.set_cost_paper(1)
    scientistsGuild.wildcard = 1
    cardList.append(scientistsGuild)

    spiesGuild = Card('Spies Guild', 0, 3, 'purple')
    spiesGuild.set_cost_brick(3)
    spiesGuild.set_cost_glass(1)
    cardList.append(spiesGuild)

    strategistsGuild = Card('Strategists Guild', 0, 3, 'purple')
    strategistsGuild.set_cost_ore(2)
    strategistsGuild.set_cost_stone(1)
    strategistsGuild.set_cost_cloth(1)
    cardList.append(strategistsGuild)

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
        for card in cardList:
            db.session.add(card)
        db.session.commit()
