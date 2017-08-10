from index import db


class Card(db.Model):
    __tablename__ = 'card'
    name = db.Column(db.String(50), primary_key=True)
    noPlayers = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, default=1)
    type = db.Column(db.String(10))

    costMoney = db.Column(db.Integer, default=0)
    costWood = db.Column(db.Integer, default=0)
    costBrick = db.Column(db.Integer, default=0)
    costOre = db.Column(db.Integer, default=0)
    costStone = db.Column(db.Integer, default=0)
    costGlass = db.Column(db.Integer, default=0)
    costPaper = db.Column(db.Integer, default=0)
    costCloth = db.Column(db.Integer, default=0)
    prerequisite1 = db.Column(db.String(30), default='')
    prerequisite2 = db.Column(db.String(30), default='')

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
    
    def __init__(self, name, noPlayers, age, type):
        self.name = name
        self.noPlayers = noPlayers
        self.age = age
        self.type = type
    
    def add_cost_money(self, money):
        self.costMoney = money
    def add_cost_wood(self, wood):
        self.costWood = wood
    def add_cost_brick(self, brick):
        self.costBrick = brick
    def add_cost_ore(self, ore):
        self.costOre = ore
    def add_cost_stone(self, stone):
        self.costStone = stone
    def add_cost_glass(self, glass):
        self.costGlass = glass
    def add_cost_paper(self, paper):
        self.costPaper = paper
    def add_cost_cloth(self, cloth):
        self.costCloth = cloth
    def add_prerequisite_1(self, prereq):
        self.prerequisite1 = prereq
    def add_prerequisite_2(self, prereq):
        self.prerequisite2 = prereq
    
    def add_benefit_wood(self, wood):
        self.giveWood = wood
    def add_benefit_brick(self, brick):
        self.giveBrick = brick
    def add_benefit_ore(self, ore):
        self.giveOre = ore
    def add_benefit_stone(self, stone):
        self.giveStone = stone
    def add_benefit_glass(self, glass):
        self.giveGlass = glass
    def add_benefit_paper(self, paper):
        self.givePaper = paper
    def add_benefit_cloth(self, cloth):
        self.giveCloth = cloth
    def set_resource_alternating(self, alt):
        self.resourceAlternating = alt
    def add_benefit_points(self, points):
        self.givePoints = points
    def add_benefit_military(self, military):
        self.giveMilitary = military
    def add_benefit_money(self, money):
        self.giveMoney = money
    def add_benefit_research(self, research):
        self.giveResearch = research