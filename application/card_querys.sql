
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