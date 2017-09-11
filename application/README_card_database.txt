NOTE AS OF 11/9/2017 ---- DEPRECATED INFORMATION

Card database containing the data for the cards in 7 Wonders.
Contains all of the information needed to deal with all cards except yellow and purple cards.

Information in database is:
name - name of the card
colour - colour of the card
age - which age the card appears in
number_of_players_for_first - how many players are needed to have at least one occurrence of the card
number_of_players_for_second - how many players are needed to have at least two occurrences of the card. If NULL, never have a second occurrence
number_of_players_for_third - how many players are needed to have at three occurrences of the card. If NULL, never have a third occurrence
resource_1 - first resource the card provides. If NULL, provides no resource
resource_2 - second resource the card provides. If NULL, does not provide a second resource
resource_alternating - If the card provides both resources simultaniously. If TRUE, only one provided resource may be used on a given turn
points - points provided by the card
research - type of research provided by the card. If NULL, no research is provided
military - military power provided by the card
cost_wood, cost_stone, cost_ore, cost_brick - brown resources required to build the card
cost_glass, cost_papyrus, cost_textiles - grey resources required to build the card
cost_money - monetary cost to build the card
prerequisite_1, prerequisite_2 - alternate cost. If either of the cards listed here have been built by the player, no resource cost is required

Example queries for obtaining cards from the database:

	--Get all cards from age 1
SELECT cards.* FROM cards WHERE cards.age = 1 AND cards.number_of_players_for_first <= 7
UNION ALL
SELECT cards.* FROM cards WHERE cards.age = 1 AND cards.number_of_players_for_second <= 7
UNION ALL
SELECT cards.* FROM cards WHERE cards.age = 1 AND cards.number_of_players_for_third <= 7

	--Get all cards from age 2
SELECT cards.* FROM cards WHERE cards.age = 2 AND cards.number_of_players_for_first <= 7
UNION ALL
SELECT cards.* FROM cards WHERE cards.age = 2 AND cards.number_of_players_for_second <= 7
UNION ALL
SELECT cards.* FROM cards WHERE cards.age = 2 AND cards.number_of_players_for_third <= 7

	--Get all cards from age 3
SELECT cards.* FROM cards WHERE cards.age = 3 AND cards.number_of_players_for_first <= 7
UNION ALL
SELECT cards.* FROM cards WHERE cards.age = 3 AND cards.number_of_players_for_second <= 7
UNION ALL
SELECT cards.* FROM cards WHERE cards.age = 3 AND cards.number_of_players_for_third <= 7
UNION ALL
(SELECT cards.* FROM cards WHERE cards.colour = 'purple' ORDER BY random() LIMIT 2+7)
