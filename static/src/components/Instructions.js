import React from 'react';
import { Card, CardText, CardHeader, CardMedia } from 'material-ui';

const Rules = (
    <div>
    <h1>GAME OVERVIEW </h1>
    <p>A game begins in Age I, continues with Age II and ends with Age III.
    Victory points are counted at the end of Age III.</p>

    <h3>Overview of an Age</h3>

    <p>At the beginning of each Age, each player gets a hand of 7 cards, dealt
    randomly (all cards from the pile for that Age are given out).
    Each Age is played over 6 game turns, in which the players will put into
    play a single card, simultaneously.</p>
    <b>1. Choose a card</b>
    <p>Each player looks at their hand without showing it to the other
    players and selects a card before placing it face down before
    them.
    Once every player has selected his or her card, they perform their
    action.</p>
    <b>2. Action</b>
    <p>Three actions are possible with the chosen card:
    <ul><li>Build the structure on the card (you cannot build the same
    structure twice): the card is placed in the player&#39;s play zone,
    face up.</li>
    <li>Build a stage of their Wonder (in the order given by the
    board, from left to right): the card is partially placed under the
    board, face down.</li>
    <li>Take 3 coins from the bank: the card is discarded, face down.</li></ul></p>
    <b>3. Move on to the next hand </b>
    <p>Each player takes the hand of cards given to them by their neighbor.
    Each player takes the hand of cards given to them by their neighbor.
    The direction of hand rotation changes with every age:
    clockwise for Age I,counter-clockwise for Age II,
    and clockwise again for Age III.
    On the sixth game turn of each Age, the last card is not passed:
    it is discarded, face down.</p>

    <h1>BUILDING IN 7 WONDERS  </h1>

    <h3>Structures</h3>
    <p><ul><li>Coin cost: the cost is paid to the bank.</li>
    <li>Free construction: the structure is built for free.</li>
    <li>Resource cost: the indicated resources are produced by the
    player&#39;s city and/or bought using the commerce rules.</li>
    <li>Free construction (chain): if, in the previous Age, a player has
    built the structure named next to the resource cost, then that
    player may build the structure for free.</li></ul></p>
    <h3>Wonder</h3>
    <p><ul><li>Resource cost: the resources indicated are produced by the
    player&#39;s city and/or bought using the commerce rules.</li></ul></p>
    <h3>Production</h3>
    <p><ul><li>The resources of a city are produced by its Wonder board, its
    brown cards, its gray cards, and by some of its yellow cards.</li>
    <li>To be able to build a structure or a stage of a Wonder without
    using commerce, a player&#39;s city must produce the resources
    indicated on the structure&#39;s card or wonder&#39;s board.</li>
    <li>Resources are not spent during construction. They can be spent
    each turn, for the entire game. A city&#39;s production can never
    decrease.</li></ul></p>
    <h3>Commerce</h3>
    <p><ul><li>Each player can only trade with the two neighboring cities.</li>
    <li>Each resource bought is paid 2 coins to its owner (players can
    never refuse trade).</li>
    <li>Selling a resource does not prevent its owner from being able
    to use it, in that same turn, for their own construction.</li></ul></p>

    <h1>END OF AN AGE </h1>
    <p>Each Age ends after its sixth game turn.
    The players must then proceed with the resolution of military conflicts.
    Each player compares the total amount of shield symbols
    present on their military structures (red cards) with the total
    of each of their neighboring cities:</p>
    <p><ul><li>If a player has a higher total than that of a
    neighboring city, that player takes a Victory token
    corresponding to the Age which just ended
    (Age I: +1, Age II: +3 or Age III: +5)</li>
    <li>If a player has a lower total than that of a
    neighboring city, that player takes a Defeat token
    (-1victory point)</li>
    <li>If a player has a total equal to that of a neighboring city, no
    tokens are taken.</li></ul></p>
    <p>During each Age, each player therefore gets, depending on the case, 0,
    1 or 2 tokens which are placed on his or her Wonder board.</p>
    <h1>END OF GAME AND SCORING </h1>
    At the end of Age III, once the conflict tokens have been handed out,
    the players total their victory points:
    <ol><li>Military Conflicts: points from Conflict tokens.</li>
    <li>Treasury Contents: 1 victory point for every 3 coins (leftover coins score no points).</li>
    <li>Wonder: points are earned as indicated on the Wonder&#39;s board.</li>
    <li>Civilian Structures: points indicated on the cards.</li>
    <li>Commercial Structures: points indicated on the cards.</li>
    <li>Guilds: points indicated on the cards.</li>
    <li>Science Structures</li></ol>
    </div>
);

const sShots = (
  <section className="clearfix">
      <h1>Game Screen Layout</h1>
      <img width="100%" border="5" src={`dist/images/screenshots/Full.png`} />
      <hr />
      <h1>Components</h1>
      <br />
      <div style={{ width: '50%', float: 'left', paddingRight: 15 }}>
          <div>
              <h4 style={{ marginTop: 15 }}>Cards In Hand</h4>
              <p>These are located at the top of your screen. On the top left of each card show inventory needed
              to build each structure. The three icons below each card represents the play actions.</p>
              <p><img width="30" style={{ marginRight: 20, marginLeft: 20 }} src={`dist/images/icons/check.png`} /><b>Play</b> the current card</p>
              <p><img width="30" style={{ marginRight: 20, marginLeft: 20 }} src={`dist/images/icons/pyramid-stage1.png`} /><b> Play for Wonder</b>,</p>
              <p><img width="30" style={{ marginRight: 20, marginLeft: 20 }} src={`dist/images/icons/trash.png`} /><b>Discard</b> current card</p>
              <img width="250" border="5" src={`dist/images/screenshots/CardInHand.png`} />
          </div>
          <div>
              <h4 style={{ marginTop: 15 }}>Trading</h4>
              <p>In order to trade your left or right player, choose the card you wish to play by clicking the <b>Play</b>
              (<img width="20" style={{ marginRight: 10, marginLeft: 10 }} src={`dist/images/icons/check.png`} />) or the <b>Wonder</b>
              (<img width="20" style={{ marginRight: 10, marginLeft: 10 }} src={`dist/images/icons/pyramid-stage1.png`} />) buttons.
              The Game will assess if you can play the card with or without the help of trading. If trading can be done, the cheapest option
              will be displayed and a <b>Confirmation</b> is required before completing the trade. You can proceed with a trade, or cancel, and your card
              will be actioned accordingly.</p>
              <img width="95%" border="5" src={`dist/images/screenshots/TradeDialog.png`} />
          </div>
          <div>
              <h4 style={{ marginTop: 15 }}>Navigating the Player Circle</h4>
              <p>This is important to see what your neighbour has build, or inventory he/she is producing.
              On either end of the player Wonder board display, click on the
              <img width="9" style={{ marginRight: 10, marginLeft: 10 }} src={`dist/images/icons/left_arrow.png`} />
              to navigate to the left of the current player, and similarly
              <img width="9" style={{ marginRight: 10, marginLeft: 10 }} src={`dist/images/icons/right_arrow.png`} /> to navigate to the right.
              A quick navigation button back to <b>YOUR WONDER</b> is displayed above the Points counter on the right
              , if you are not currently viewing your wonder </p>
          </div>
      </div>
      <div style={{ width: '50%', float: 'left'}}>
          <div className="clearfix">
              <h4 style={{ marginTop: 15 }}>Inventory</h4>
              <img height="300" style={{ float: 'right'}} border="5" src={`dist/images/screenshots/Inventory.png`} />
              <p style={{ float: 'left', width: '65%' }}>This summary Table will display the inventory for the currently displayed player.
              The first number for each inventory represents inventory produced for a single turns
              The second number relates to the split inventory card. For instance, the diagram shows
              that a split card has been played for this player, where the card yields one Wood or one Brick per turn.
              Best to double check your card history to check which split cards are played  </p>
          </div>
          <div>
              <h4 style={{ marginTop: 15 }}>Completing Wonder Stages</h4>
              <p>To build a wonder stage, you need to select a card from your hand by clicking on the <b>Wonder</b>
              (<img width="20" style={{ marginRight: 10, marginLeft: 10 }} src={`dist/images/icons/pyramid-stage1.png`} />) button.
              If trade is needed, confirm payment, and card will be played for the Wonder, showing <b>Complete</b> on the next
              stage. These are completed in order.</p>
              <img width="300" border="5" src={`dist/images/screenshots/Completed.png`} />
          </div>
          <div>
              <h4 style={{ marginTop: 15 }}>Card History</h4>
              <p>This can be found below the current players wonder board by a drop down button. This is useful to see
              what cards the current player has played and what structures are built. Also helpful to gain a better insight
              on the split inventory cards for your next turn. (note: Discarded cards and cards played for Wonders will not show here)</p>
              <img width="95%" border="5" src={`dist/images/screenshots/History.png`} />
          </div>
          <div>
              <h4 style={{ marginTop: 15 }}>Age progress counter</h4>
              <p>This is helpful to know how far through each Age you are</p>
              <center><img width="150" border="5" src={`dist/images/screenshots/AgeProgress.png`} /></center>
          </div>
          <div>
          <h4 style={{ marginTop: 15 }}>End Game</h4>
          <p>If you want to finish the game early, button is located in the top right of the screen</p>
          <img width="300" border="5" src={`dist/images/screenshots/EndGame.png`} />
          </div>
      </div>
  </section>
);



const Instructions = () => (
    <div className="row">
        <div className="col-md-8 offset-md-2 col-sm-12 col-sm-offset-0">
          <h1>How to play...</h1>
            <p> Below are some instructions on how to play 7 Wonders</p>
            <p> From original game manual to navigating around our <i>Online Capstone Edition 2017</i> </p>
            <br />
            <Card style={{ width: '100%' }}>
                <CardHeader
                    title="Original Quick Rules and Gameplay"
                    actAsExpander={true}
                    showExpandableButton={true}
                />
                <CardText expandable={true} style={{ height: 'auto' }}>
                    <CardMedia>
                        {Rules}
                    </CardMedia>
                </CardText>
            </Card>
            <br />
            <Card style={{ width: '100%' }}>
                <CardHeader
                    title="Navigating 7 Wonders Online Capstone Edition 2017"
                    actAsExpander={true}
                    showExpandableButton={true}
                />
                <CardText expandable={true} style={{ height: 'auto' }}>
                    <CardMedia>
                        {sShots}
                    </CardMedia>
                </CardText>
            </Card>
            <br />
            <Card style={{ width: '100%' }}>
                <CardHeader
                    title="Tutorial Video"
                    actAsExpander={true}
                    showExpandableButton={true}
                />
                <CardText expandable={true} style={{ height: 'auto' }}>
                    <CardMedia>
                        <div class="videoWrapper">
                            <iframe
                                width="560"
                                height="315"
                                src="https://www.youtube.com/embed/OAQKdgfZvXI"
                                frameborder="0"
                                gesture="media" allowfullscreen>
                            </iframe>
                        </div>
                    </CardMedia>
                </CardText>
            </Card>
        </div>
    </div>
);

export default Instructions;
