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



const Instructions = () => (
    <div className="col-md-8" style={{ marginLeft: 100 }}>
      <h1>How to play...</h1>
        <p> Below are some instructions on how to play 7 Wonders</p>
        <p> From original game manual to navigating around our <i>Online Capstone Edition 2017</i> </p>
        <br />
        <Card style={{ width: '100%' }}>
            <CardHeader
                title="Quick Rules and Gameplay"
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
                title="ScreenShots"
                actAsExpander={true}
                showExpandableButton={true}
            />
            <CardText expandable={true} style={{ height: 450 }}>
                <p> Please Note: Proper Screen shots to come. Below is an example </p>
                <CardMedia>
                    <embed
                        alt='Screen Capture - Game Screen'
                        src='dist/images/background/capture.jpg'
                        style={{ height: 400 }}
                    />
                </CardMedia>
            </CardText>
        </Card>
    </div>
);

export default Instructions;
