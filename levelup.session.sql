SELECT * FROM levelupapi_gametype;

SELECT * FROM auth_user;
SELECT * FROM authtoken_token;
SELECT * FROM levelupapi_gamer;

SELECT * FROM levelupapi_event;

SELECT * FROM levelupapi_game;

SELECT * FROM levelupapi_gamer;
SELECT * FROM levelupapi_event e JOIN levelupapi_game g
ON e.game_id = g.id WHERE g.id=1

SELECT
    title,
    maker,
    number_of_players,
    skill_level,
    gamer_id,
    gametype_id
FROM
    levelupapi_game
WHERE
    id = 3