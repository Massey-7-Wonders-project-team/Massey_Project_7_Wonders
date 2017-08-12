from index import db


class Card(db.Model):
    __tablename__ = 'card'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    noPlayers = db.Column(db.Integer)
    age = db.Column(db.Integer)
    colour = db.Column(db.String(10))

    costMoney = db.Column(db.Integer, default=0)
    costWood = db.Column(db.Integer, default=0)
    costBrick = db.Column(db.Integer, default=0)
    costOre = db.Column(db.Integer, default=0)
    costStone = db.Column(db.Integer, default=0)
    costGlass = db.Column(db.Integer, default=0)
    costPaper = db.Column(db.Integer, default=0)
    costCloth = db.Column(db.Integer, default=0)
    prerequisite1 = db.Column(db.String(50), default='')
    prerequisite2 = db.Column(db.String(50), default='')

    giveWood = db.Column(db.Integer, default=0)
    giveBrick = db.Column(db.Integer, default=0)
    giveOre = db.Column(db.Integer, default=0)
    giveStone = db.Column(db.Integer, default=0)
    giveGlass = db.Column(db.Integer, default=0)
    givePaper = db.Column(db.Integer, default=0)
    giveCloth = db.Column(db.Integer, default=0)
    resourceAlternating = db.Column(db.Boolean, default=False)
    givePoints = db.Column(db.Integer, default=0)
    giveMilitary = db.Column(db.Integer, default=0)
    giveMoney = db.Column(db.Integer, default=0)
    giveResearch = db.Column(db.String(10), default='')
    
    def __init__(self, name, noPlayers, age, colour):
        self.name = name
        self.noPlayers = noPlayers
        self.age = age
        self.colour = colour
    
    def set_cost_money(self, money):
        self.costMoney = money
    def set_cost_wood(self, wood):
        self.costWood = wood
    def set_cost_brick(self, brick):
        self.costBrick = brick
    def set_cost_ore(self, ore):
        self.costOre = ore
    def set_cost_stone(self, stone):
        self.costStone = stone
    def set_cost_glass(self, glass):
        self.costGlass = glass
    def set_cost_paper(self, paper):
        self.costPaper = paper
    def set_cost_cloth(self, cloth):
        self.costCloth = cloth
    def set_prerequisite_1(self, prereq):
        self.prerequisite1 = prereq
    def set_prerequisite_2(self, prereq):
        self.prerequisite2 = prereq

    def set_benefit_wood(self, wood):
        self.giveWood = wood
    def set_benefit_brick(self, brick):
        self.giveBrick = brick
    def set_benefit_ore(self, ore):
        self.giveOre = ore
    def set_benefit_stone(self, stone):
        self.giveStone = stone
    def set_benefit_glass(self, glass):
        self.giveGlass = glass
    def set_benefit_paper(self, paper):
        self.givePaper = paper
    def set_benefit_cloth(self, cloth):
        self.giveCloth = cloth
    def set_resource_alternating(self, alt):
        self.resourceAlternating = alt
    def set_benefit_points(self, points):
        self.givePoints = points
    def set_benefit_military(self, military):
        self.giveMilitary = military
    def set_benefit_money(self, money):
        self.giveMoney = money
    def set_benefit_research(self, research):
        self.giveResearch = research
