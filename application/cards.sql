CREATE TABLE cards(

	--card details
	name varchar(20),
	colour varchar(20),
	age integer,
	number_of_players_for_first integer,
	number_of_players_for_second integer,
	number_of_players_for_third integer,
	
	--provides
	resource_1 varchar(20),
	resource_2 varchar(20),
	resource_alternating boolean,
	points integer,
	research varchar(20),
	military varchar(20),
	--yellow & guilds in python
	
	--costs
	cost_wood integer,
	cost_stone integer,
	cost_ore integer,
	cost_brick integer,
	cost_glass integer,
	cost_papyrus integer,
	cost_textiles integer,
	cost_money integer,
	prerequisite_1 varchar(20),
	prerequisite_2 varchar(20),
	PRIMARY KEY (name, age)
);

INSERT INTO cards (name, colour, age, number_of_players_for_first, number_of_players_for_second, number_of_players_for_third,
					resource_1, resource_2, resource_alternating, points, research, military,
					cost_wood, cost_stone, cost_ore, cost_brick, cost_glass, cost_papyrus, cost_textiles, cost_money, prerequisite_1, prerequisite_2)
VALUES
		--!!!!!!!!!!!!!!
		--age 1
		--!!!!!!!!!!!!!!
		
		--age 1 browns
		('Lumber Yard', 'brown', 1, 3, 4, NULL,
		'wood', NULL, FALSE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL),
			
		('Stone Pit', 'brown', 1, 3, 5, NULL,
		'stone', NULL, FALSE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		('Clay Pool', 'brown', 1, 3, 5,	NULL,
		'brick', NULL, FALSE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		('Ore Vein', 'brown', 1, 3, 4, NULL,
		'ore', NULL, FALSE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		('Tree Farm', 'brown', 1, 6, NULL, NULL,
		'wood', 'brick', TRUE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 1, NULL, NULL),
		
		('Excavation', 'brown', 1, 4, NULL, NULL,
		'stone', 'brick', TRUE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 1, NULL, NULL),
		
		('Clay Pit', 'brown', 1, 3, NULL, NULL,
		'brick', 'ore', TRUE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 1, NULL, NULL),
		
		('Timber Yard', 'brown', 1, 3, NULL, NULL,
		'stone', 'wood', TRUE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 1, NULL, NULL),
		
		('Forest Cave', 'brown', 1, 5, NULL, NULL,
		'wood', 'ore', TRUE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 1, NULL, NULL),
		
		('Mine', 'brown', 1, 6, NULL, NULL,
		'ore', 'stone', TRUE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 1, NULL, NULL),
		
		--age 1 greys
		('Loom', 'grey', 1, 3, 6, NULL,
		'textile', NULL, FALSE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		('Glassworks', 'grey', 1, 3, 6, NULL,
		'glass', NULL, FALSE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		('Press', 'grey', 1, 3, 6, NULL,
		'papyrus', NULL, FALSE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		--age 1 blues
		('Pawnshop', 'blue', 1, 4, 7, NULL,
		NULL, NULL, FALSE, 3, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		('Baths', 'blue', 1, 3, 7, NULL,
		NULL, NULL, FALSE, 3, NULL, 0,
		0, 1, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		('Altar', 'blue', 1, 3, 5, NULL,
		NULL, NULL, FALSE, 2, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		('Theater', 'blue', 1, 3, 6, NULL,
		NULL, NULL, FALSE, 2, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		--age 1 yellows
		('Tavern', 'yellow', 1, 4, 5, 7,
		NULL, NULL, FALSE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		('East Trading Post', 'yellow', 1, 3, 7, NULL,
		NULL, NULL, FALSE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		('West Trading Post', 'yellow', 1, 3, 7, NULL,
		NULL, NULL, FALSE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		('Marketplace', 'yellow', 1, 3, 6, NULL,
		NULL, NULL, FALSE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		--age 1 reds
		('Stockade', 'red', 1, 3, 7, NULL,
		NULL, NULL, FALSE, 0, NULL, 1,
		1, 0, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		('Barracks', 'red', 1, 3, 5, NULL,
		NULL, NULL, FALSE, 0, NULL, 1,
		0, 0, 1, 0, 0, 0, 0, 0, NULL, NULL),
		
		('Guard Tower', 'red', 1, 3, 4, NULL,
		NULL, NULL, FALSE, 0, NULL, 1,
		0, 0, 0, 1, 0, 0, 0, 0, NULL, NULL),
		
		--age 1 greens
		('Apothecary', 'green', 1, 3, 5, NULL,
		NULL, NULL, FALSE, 0, 'compass', 0,
		0, 0, 0, 0, 0, 0, 1, 0, NULL, NULL),
		
		('Workshop', 'green', 1, 3, 7, NULL,
		NULL, NULL, FALSE, 0, 'cog', 0,
		0, 0, 0, 0, 1, 0, 0, 0, NULL, NULL),
		
		('Scriptorium', 'green', 1, 3, 4, NULL,
		NULL, NULL, FALSE, 0, 'tablet', 0,
		0, 0, 0, 0, 0, 1, 0, 0, NULL, NULL),
		
		--!!!!!!!!!!!!!!
		--age 2
		--!!!!!!!!!!!!!!
		
		--age 2 browns
		('Sawmill', 'brown', 2, 3, 4, NULL,
		'wood', 'wood', FALSE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 1, NULL, NULL),
			
		('Quarry', 'brown', 2, 3, 4, NULL,
		'stone', 'stone', FALSE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 1, NULL, NULL),
		
		('Brickyard', 'brown', 2, 3, 4, NULL,
		'brick', 'brick', FALSE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 1, NULL, NULL),
		
		('Foundry', 'brown', 2, 3, 4, NULL,
		'ore', 'ore', FALSE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 1, NULL, NULL),
		
		--age 2 greys
		('Loom', 'grey', 2, 3, 5, NULL,
		'textile', NULL, FALSE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		('Glassworks', 'grey', 2, 3, 5, NULL,
		'glass', NULL, FALSE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		('Press', 'grey', 2, 3, 5, NULL,
		'papyrus', NULL, FALSE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		--age 2 blues
		('Aqueduct', 'blue', 2, 3, 7, NULL,
		NULL, NULL, FALSE, 5, NULL, 0,
		0, 3, 0, 0, 0, 0, 0, 0, 'Baths', NULL),
		
		('Temple', 'blue', 2, 3, 6, NULL,
		NULL, NULL, FALSE, 3, NULL, 0,
		1, 0, 0, 1, 1, 0, 0, 0, 'Altar', NULL),
		
		('Statue', 'blue', 2, 3, 7, NULL,
		NULL, NULL, FALSE, 4, NULL, 0,
		1, 0, 2, 0, 0, 0, 0, 0, 'Theater', NULL),
		
		('Courthouse', 'blue', 2, 3, 5, NULL,
		NULL, NULL, FALSE, 4, NULL, 0,
		0, 0, 0, 2, 0, 0, 1, 0, 'Scriptorium', NULL),
		
		--age 2 yellows
		('Forum', 'yellow', 2, 3, 6, 7,
		NULL, NULL, TRUE, 0, NULL, 0,
		0, 0, 0, 2, 0, 0, 0, 0, 'East Trading Post', 'West Trading Post'),
		
		('Caravansery', 'yellow', 2, 3, 5, 6,
		NULL, NULL, TRUE, 0, NULL, 0,
		2, 0, 0, 0, 0, 0, 0, 0, 'Marketplace', NULL),
		
		('Vineyard', 'yellow', 2, 3, 6, NULL,
		NULL, NULL, FALSE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		('Bazar', 'yellow', 2, 4, 7, NULL,
		NULL, NULL, FALSE, 0, NULL, 0,
		0, 0, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		--age 2 reds
		('Walls', 'red', 2, 3, 7, NULL,
		NULL, NULL, FALSE, 0, NULL, 2,
		0, 3, 0, 0, 0, 0, 0, 0, NULL, NULL),
		
		('Training Ground', 'red', 2, 4, 6, 7,
		NULL, NULL, FALSE, 0, NULL, 2,
		1, 0, 2, 0, 0, 0, 0, 0, NULL, NULL),
		
		('Stables', 'red', 2, 3, 5, NULL,
		NULL, NULL, FALSE, 0, NULL, 2,
		1, 0, 1, 1, 0, 0, 0, 0, NULL, NULL),
		
		('Archery Range', 'red', 2, 3, 6, NULL,
		NULL, NULL, FALSE, 0, NULL, 2,
		2, 0, 1, 0, 0, 0, 0, 0, NULL, NULL),
		
		--age 2 greens
		('Dispensary', 'green', 2, 3, 4, NULL,
		NULL, NULL, FALSE, 0, 'compass', 0,
		0, 0, 2, 0, 1, 0, 0, 0, 'Apothecary', NULL),
		
		('Laboratory', 'green', 2, 3, 5, NULL,
		NULL, NULL, FALSE, 0, 'cog', 0,
		0, 0, 0, 2, 0, 1, 0, 0, 'Workshop', NULL),
		
		('Library', 'green', 2, 3, 6, NULL,
		NULL, NULL, FALSE, 0, 'tablet', 0,
		0, 2, 0, 0, 0, 0, 1, 0, 'Scriptorium', NULL),
		
		('School', 'green', 2, 3, 7, NULL,
		NULL, NULL, FALSE, 0, 'tablet', 0,
		1, 0, 0, 0, 1, 0, 0, 0, NULL, NULL),
		
		--!!!!!!!!!!!!!!
		--age 3
		--!!!!!!!!!!!!!!
		
		--age 3 blues
		('Pantheon', 'blue', 3, 3, 6, NULL,
		NULL, NULL, FALSE, 7, NULL, 0,
		0, 0, 1, 2, 1, 1, 1, 0, 'Temple', NULL),
		
		('Gardens', 'blue', 3, 3, 4, NULL,
		NULL, NULL, FALSE, 5, NULL, 0,
		1, 0, 0, 2, 0, 0, 0, 0, 'Statue', NULL),
		
		('Town Hall', 'blue', 3, 3, 5, 6,
		NULL, NULL, FALSE, 6, NULL, 0,
		0, 2, 1, 0, 1, 0, 0, 0, NULL, NULL),
		
		('Palace', 'blue', 3, 3, 7, NULL,
		NULL, NULL, FALSE, 8, NULL, 0,
		1, 1, 1, 1, 1, 1, 1, 0, NULL, NULL),
		
		('Senate', 'blue', 3, 3, 5, NULL,
		NULL, NULL, FALSE, 6, NULL, 0,
		2, 1, 1, 0, 0, 0, 0, 0, 'Library', NULL),
		
		--age 3 yellows
		('Haven', 'yellow', 3, 3, 4, NULL,
		NULL, NULL, FALSE, 0, NULL, 0,
		1, 0, 1, 0, 0, 0, 1, 0, 'Forum', NULL),
		
		('Lighthouse', 'yellow', 3, 3, 6, NULL,
		NULL, NULL, FALSE, 0, NULL, 0,
		0, 1, 0, 0, 1, 0, 0, 0, 'Caravansery', NULL),
		
		('Chamber Of Commerce', 'yellow', 3, 4, 6, NULL,
		NULL, NULL, FALSE, 0, NULL, 0,
		0, 0, 0, 2, 0, 1, 0, 0, NULL, NULL),
		
		('Arena', 'yellow', 3, 3, 5, 7,
		NULL, NULL, FALSE, 0, NULL, 0,
		0, 2, 1, 0, 0, 0, 0, 0, 'Dispensary', NULL),
		
		--age 3 reds
		('Fortifications', 'red', 3, 3, 7, NULL,
		NULL, NULL, FALSE, 0, NULL, 3,
		0, 1, 3, 0, 0, 0, 0, 0, 'Walls', NULL),
		
		('Circus', 'red', 3, 4, 5, 6,
		NULL, NULL, FALSE, 0, NULL, 3,
		0, 3, 1, 0, 0, 0, 0, 0, 'Training Ground', NULL),
		
		('Arsenal', 'red', 3, 3, 4, 7,
		NULL, NULL, FALSE, 0, NULL, 3,
		2, 0, 1, 0, 0, 0, 1, 0, NULL, NULL),
		
		('Siege Workshop', 'red', 3, 3, 5, NULL,
		NULL, NULL, FALSE, 0, NULL, 3,
		1, 0, 0, 3, 0, 0, 0, 0, 'Laboratory', NULL),
		
		--age 3 greens
		('Lodge', 'green', 3, 3, 6, NULL,
		NULL, NULL, FALSE, 0, 'compass', 0,
		0, 0, 0, 2, 0, 1, 1, 0, 'Dispensary', NULL),
		
		('Observatory', 'green', 3, 3, 7, NULL,
		NULL, NULL, FALSE, 0, 'cog', 0,
		0, 0, 2, 0, 1, 0, 1, 0, 'Laboratory', NULL),
		
		('University', 'green', 3, 3, 4, NULL,
		NULL, NULL, FALSE, 0, 'tablet', 0,
		2, 0, 0, 0, 1, 1, 0, 0, 'Library', NULL),
		
		('Academy', 'green', 3, 3, 7, NULL,
		NULL, NULL, FALSE, 0, 'compass', 0,
		0, 3, 0, 0, 1, 0, 0, 0, 'School', NULL),
		
		('Study', 'green', 3, 3, 5, NULL,
		NULL, NULL, FALSE, 0, 'cog', 0,
		1, 0, 0, 0, 0, 1, 1, 0, 'School', NULL),
		
		--purples (guilds)
		('Workers Guild', 'purple', 3, NULL, NULL, NULL,
		NULL, NULL, FALSE, 0, NULL, 0,
		1, 1, 2, 1, 0, 0, 0, 0, NULL, NULL),
		
		('Craftmens Guild', 'purple', 3, NULL, NULL, NULL,
		NULL, NULL, FALSE, 0, NULL, 0,
		0, 2, 2, 0, 0, 0, 0, 0, NULL, NULL),
		
		('Traders Guild', 'purple', 3, NULL, NULL, NULL,
		NULL, NULL, FALSE, 0, NULL, 0,
		0, 0, 0, 0, 1, 1, 1, 0, NULL, NULL),
		
		('Philosophers Guild', 'purple', 3, NULL, NULL, NULL,
		NULL, NULL, FALSE, 0, NULL, 0,
		0, 0, 0, 3, 0, 1, 1, 0, NULL, NULL),
		
		('Spy Guild', 'purple', 3, NULL, NULL, NULL,
		NULL, NULL, FALSE, 0, NULL, 0,
		0, 0, 0, 3, 1, 0, 0, 0, NULL, NULL),
		
		('Strategy Guild', 'purple', 3, NULL, NULL, NULL,
		NULL, NULL, FALSE, 0, NULL, 0,
		0, 1, 2, 0, 0, 0, 1, 0, NULL, NULL),
		
		('Shipowners Guild', 'purple', 3, NULL, NULL, NULL,
		NULL, NULL, FALSE, 0, NULL, 0,
		3, 0, 0, 0, 1, 1, 0, 0, NULL, NULL),
		
		('Scientists Guild', 'purple', 3, NULL, NULL, NULL,
		NULL, NULL, FALSE, 0, NULL, 0,
		2, 0, 2, 0, 1, 0, 0, 0, NULL, NULL),
		
		('Magistrates Guild', 'purple', 3, NULL, NULL, NULL,
		NULL, NULL, FALSE, 0, NULL, 0,
		3, 1, 0, 0, 0, 0, 1, 0, NULL, NULL),
		
		('Builders Guild', 'purple', 3, NULL, NULL, NULL,
		NULL, NULL, FALSE, 0, NULL, 0,
		0, 2, 0, 2, 1, 0, 0, 0, NULL, NULL);
