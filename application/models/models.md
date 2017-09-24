Updated 24/09/2017 by Jacob Stringer
Created 11/09/2017 by Jacob Stringer

# Execution
All model classes in the models folder rely on the ORM SQLAlchemy. In order to run them, manage.py create_db function
needs to be called, as explained in the root folder's README.md.

In order to create objects that use Alchemy, you can either use the class constructor, or use Alchemy's constructor
style. If using this second method, you will need to define kwargs in the constructor which match the foreign keys and
any primary keys. In almost all models, the first field is an id, which Alchemy automatically defines as a number
incremented from 1 with each additional object of the type created. As Alchemy requires primary keys, any models which
otherwise would only need foreign keys to be semantically correct use the id as the primary key.


# Details

## Read-only models
- **Card:**
The card object includes all the information about cards in one object - including its name, costs, benefits, and
any other pertinent information. Wonder slots are also implemented as cards under the hood, discussed in more detail
next. Cards should not be mutated in any function. To populate the db, create_db calls the cards_setup which adds into
the database all cards, wonder information and AI users.

- **Wonder:**
The wonder object ties together the name of the wonder along with its maximum slots and the names of its cards.


Immutable models that should not be adjusted:
- Wonder (manage.create_db calls cards_setup)
- Card (manage.create_db calls cards_setup)

Immutable from in-game's perspective after setup:
- User (created by authentication process)
- Game (created by application.app.create_game())

Mutable from in-game:
- Player (created by application.app.create_game())
Player stores all current state information for a player
- Round
Round stores hand information. When searched by a round, age and player, it will return that player's hand
- Cardhist
Stores how cards have been played so far. Searching this table by player will return all cards played.
Specify not discarded to avoid discard pile. Search by discarded for every player to return discard pile.
Does not include cards that are used for wonder construction - the wonder cards will be in here instead.

