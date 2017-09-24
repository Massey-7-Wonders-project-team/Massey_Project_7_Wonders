Created 2017/09/21 by Jacob Stringer

Structure of controllers files:


                app.py
                /    \
               /      \
     card_logic.py     state_printer.py
     /          |                     |
    /           |                    /
ai.py     game_state_functions.py   /
   \            |                  /
    \           |                 /
      ---database_functions.py---


This is the importing hierarchy. Files import only the files directly underneath them. I created this hierarchy to
prevent troublesome circular imports.

1. app.py
This is the API gateway. It accepts all calls from the front end. It uses game_state to set up the game, then card_logic
to change the state of the game. It calls state_printer to get the dictionary giving the game's state information.
TODO - use the database_function methods to replace the DB calls in app.py to simplify code
TODO - take advantage of print_json's new optional variables so that any unnecessary DB calls in app.py can be taken out

2. state_printer.py
This set of functions assists app.py in cleaning incoming data and getting output data ready. They do not change the
state of the game.

3. card_logic.py
This set of functions deals with playing cards. The main function here is process_card, which maps moves to many other
functions. Understanding this function is enough to understand the entire card playing sequence.
- DB Query Refactor Completed

4. ai.py
This file contains AI logic to make their card choices smarter. Currently it is only a stub awaiting further development.
TODO - create scoring for cards so the best card can be chosen for a given turn

5. game_state_functions.py
This file contains functions to set up the game and the functions that update the game object (round and age increments),
player object, and the associated calculations needed for both (like research and military calculations).
- DB Query Refactor Completed

6. database_functions.py
This file contains the db_committing_function that each of the other files use. It also imports all the models, which
are then used by others higher up the hierarchy. Increasingly, I am moving and standardising all the database calls to
getters in this file to clean up the back end code base. Others will be needed as the refactoring process happens.
TODO - add DB calling getters as needed by refactoring process
