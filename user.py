from index import db, bcrypt


class Card(db.Model):
    __tablename__ = 'card'
    name = db.Column(db.String(50), primary_key=True)
    noPlayers = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    type = db.Column(db.String(10))

    costMoney = db.Column(db.Integer)
    costWood = db.Column(db.Integer)
    costBrick = db.Column(db.Integer)
    costOre = db.Column(db.Integer)
    costStone = db.Column(db.Integer)
    costGlass = db.Column(db.Integer)
    costPaper = db.Column(db.Integer)
    costCloth = db.Column(db.Integer)

    giveWood = db.Column(db.Integer)
    giveBrick = db.Column(db.Integer)
    giveOre = db.Column(db.Integer)
    giveStone = db.Column(db.Integer)
    giveGlass = db.Column(db.Integer)
    givePaper = db.Column(db.Integer)
    giveCloth = db.Column(db.Integer)
    givePoints = db.Column(db.Integer)
    giveMilitary = db.Column(db.Integer)
    giveMoney = db.Column(db.Integer)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    cards = db.relationship(db.Card, backref='user')

    wood = db.Column(db.Integer)
    brick = db.Column(db.Integer)
    ore = db.Column(db.Integer)
    stone = db.Column(db.Integer)
    glass = db.Column(db.Integer)
    paper = db.Column(db.Integer)
    cloth = db.Column(db.Integer)
    points = db.Column(db.Integer)
    military = db.Column(db.Integer)
    money = db.Column(db.Integer)

    def __init__(self, email, password):
        self.email = email
        self.active = True
        self.password = User.hashed_password(password)
        self.game_id = None

    @staticmethod
    def hashed_password(password):
        return bcrypt.generate_password_hash(password).decode('utf-8')

    @staticmethod
    def get_user_with_email_and_password(email, password):
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return None
