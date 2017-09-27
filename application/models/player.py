from index import db
from .game import Game
from .user import User


class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True)
    gameId = db.Column(db.Integer, db.ForeignKey('game.id'))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    ready = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(255), default='')
    ai = db.Column(db.Boolean, default=False)

    left_id = db.Column(db.Integer)
    right_id = db.Column(db.Integer)

    left_cheap_trade = db.Column(db.Boolean, default=False)
    right_cheap_trade = db.Column(db.Boolean, default=False)
    advanced_cheap_trade = db.Column(db.Boolean, default=False)
    play_twice = db.Column(db.Boolean, default=False)

    wonder = db.Column(db.String(50), default='')
    wonder_level = db.Column(db.Integer, default=0)
    max_wonder = db.Column(db.Integer, default=0)

    wood = db.Column(db.Integer, default=0)
    brick = db.Column(db.Integer, default=0)
    ore = db.Column(db.Integer, default=0)
    stone = db.Column(db.Integer, default=0)
    glass = db.Column(db.Integer, default=0)
    paper = db.Column(db.Integer, default=0)
    cloth = db.Column(db.Integer, default=0)
    points = db.Column(db.Integer, default=0)
    military = db.Column(db.Integer, default=0)
    money = db.Column(db.Integer, default=3)

    cog = db.Column(db.Integer, default=0)
    tablet = db.Column(db.Integer, default=0)
    compass = db.Column(db.Integer, default=0)
    wildcard = db.Column(db.Integer, default=0)

    military_loss = db.Column(db.Integer, default=0)

    extra_wood = db.Column(db.Integer, default=0)
    extra_brick = db.Column(db.Integer, default=0)
    extra_ore = db.Column(db.Integer, default=0)
    extra_stone = db.Column(db.Integer, default=0)
    extra_glass = db.Column(db.Integer, default=0)
    extra_paper = db.Column(db.Integer, default=0)
    extra_cloth = db.Column(db.Integer, default=0)

    def __eq__(self, other):
        if type(self) is type(other):
            return self.id == other.id
        else:
            return False

    def serialise(self):
        return {
            'id':self.id,
            'gameId':self.gameId,
            'userId':self.userId,
            'profile':self.name,
            'ai':self.ai,
            'ready':self.ready,
            'left_id':self.left_id,
            'right_id':self.right_id,
            'wonder':self.wonder,
            'wonder_level':self.wonder_level,
            'max_wonder':self.max_wonder,
            'left_cheap_trade': self.left_cheap_trade,
            'right_cheap_trade': self.right_cheap_trade,
            'advanced_cheap_trade': self.advanced_cheap_trade,
            'play_twice': self.play_twice,
            'wood':self.wood,
            'brick':self.brick,
            'ore':self.ore,
            'stone':self.stone,
            'glass':self.glass,
            'paper':self.paper,
            'cloth':self.cloth,
            'extra_wood': self.extra_wood,
            'extra_brick': self.extra_brick,
            'extra_ore': self.extra_ore,
            'extra_stone': self.extra_stone,
            'extra_glass': self.extra_glass,
            'extra_paper': self.extra_paper,
            'extra_cloth': self.extra_cloth,
            'points':self.points,
            'military':self.military,
            'military_loss':self.military_loss,
            'money':self.money,
            'cog':self.cog,
            'tablet':self.tablet,
            'compass':self.compass,
            'wildcard':self.wildcard
        }
