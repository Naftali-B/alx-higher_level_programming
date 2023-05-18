-- a script that uses the hbtn_0d_tvshows database
-- to list all genres not linked to the show Dexter

SELECT tv_genres.name
FROM tv_genres
LEFT JOIN tv_shows ON tv_genres.id = tv_shows.genre_id
WHERE tv_shows.title != 'Dexter' OR tv_shows.title IS NULL
ORDER BY tv_genres.name ASC;
