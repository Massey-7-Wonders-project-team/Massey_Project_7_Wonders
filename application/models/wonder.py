from index import db


class Wonder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), default='')
    slots = db.Column(db.Integer, default=0)
    card_0 = db.Column(db.String(30), default='')
    card_1 = db.Column(db.String(30), default='')
    card_2 = db.Column(db.String(30), default='')
    card_3 = db.Column(db.String(30), default='')
    card_4 = db.Column(db.String(30), default='')

    def serialise(self):
        return {
            'id':self.id,
            'name':self.name,
            'card_0':self.card_0,
            'card_1':self.card_1,
            'card_2':self.card_2,
            'card_3': self.card_3,
            'card_4': self.card_4,
        }
