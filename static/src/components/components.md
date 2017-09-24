# This is a break down of functionality within the Components Folder

Updated:  24/09/2017
By:       Marthijn Batlajeri

##Footer/index.js:
Footer Information

##Footer/styles.scss:    
Footer Styling

##Header/index.js:
This file consists of the following functionality:
- App bar: Title, Logged in user display
- Drop down Menu:
  - Logo
  - Signed in user
  - Play link
  - How to Play link
  - Home link
  - Log out option - Signs current user out
  
##Home/index.js
Displays the first page of the application

##AuthenticatedComponent.js:  
This sends a get request to server to check if current user is Authenticated, and processes the reply

##Components.md:      
This current document file

##DetermineAuth.js:   
Checks the browsers current token for this app, and sends to server to check if still current. (Valid only for 2 weeks)

##GameScreen.js:
The main screen where the process of the game run off. This screen is actioned after a current game is deduced/created on the server and returned to browser. Functionality:
- Before game starts:
   - User clicks 'I am Ready' to play the game
   - Information displayed on how many players logged in the game
- Game in play:
   - Displays cards in hand
   - Displays selected card to play
   - Link to PlayerDisplay.js - Displays players boards/stats
- Error display if failure to load game

##Instructions.js:
Contains information regarding:
- How to play the (board) game
- (Will add) How to navigate the screen

##Inventory.js
This is linked into playerDisplay.js where this creates the statistics tabs

##LoginView.js:
Class that renders how the Login screen displays and gathers information to pass to servers

##notAuthenticatedComponent.js:
Evaluates and displays information when Users are not Logged in to the application

##NotFound.js:
Displays message when request returned not Found

##Play.js:
The screen to create/join a game after user has logged in successfully. Functionality:
- User option to create or join (if a game is created but not started) a game.
- Single player option - with a Checkbox. Player still needs to click create game after box is
 checked. This will create a 7 player game with current user and 6 computer participants
- End game button is rendered here. This helps to finish a game quicker and at any point of the game.

##PlayerDisplay.js:
This file is rendering all information about the current status of each player on the top half of GameScreen. Functions include:
- Display wonder board of current player
- Stat summaries (inventory, card type, coins, VPs, etc)
- Navigation around the player circle with left/right buttons
- Direct to users own Wonder
- Wonder card displayed
- Drop down section for played cards (cards not rendered yet)

##ProtectedView.js:
This is the Welcome screen when users are logged in successfully. Displaying current users profile name & email

##RegisterView.js:
Displays the look and feel of the register screen. Gathering information to send to server, and processing its returned status.

##Wonder.js:
This displays cards underneath the wonder board when a card is played for the wonder. This is linked from the playerDisplay class.
