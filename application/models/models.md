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
The wonder object ties together the name of the wonder along with its maximum slots and the names of its cards. Upon
dealing wonders to players, the wonder name and max slots information is copied over to the player object for ease of
use. The names of the wonder cards are listed in the wonder object so that the cards can be retrieved with the linked
names.


## Setup models
- **User**
The user object is created by Flask's authentication process, and allows for a user to play in many games. 
It has been adjusted to include usernames for display purposes. After creation, it does not change any more.

- **Game**
The game object is created to connect multiple players together in one game. It also tracks the overall state
information of the game, such as whether the game has begun and/or finished, and the current age and round. It 
gets updated periodically at game milestones, such as starting and ending the game, and incrementing rounds and ages.
It is created by the create_game API in app.py.


## Models for controlling game status
- **Player**
A unique player object binds a user to a specific game. This player object's job is to track the 
state of the player within the game, and thus includes information like resources and wonder information. The only
gotcha for this object is that there are extra_resources which arise because of resourcing alternating cards, where
you can only use some cards or the other. If these resources are required to play a card, it's necessary to find the
resource alternating cards in the cardhist model and then card model to get the specific resources provided, as 
Alchemy doesn't allow lists to easily be stored.

- **Round**
The round model specifies a player's hand in a given round. As it has a 1 to many relationship with card, multiple 
round objects will be created for every hand, so querying with an .all() function is necessary. With the round object,
the card ids can be taken, and then used to collect card objects.

- **Cardhist**
The cardhist model tracks played cards, and so links players to cards and attaches information about how they were
played such as if they were discarded (important for card resurrection) or for wonders. One gotcha for this object is
that when a card is played for a wonder, the wonder card replaces it, so the original card is not included in the
history log (as its details are no longer needed for any later game mechanics).
