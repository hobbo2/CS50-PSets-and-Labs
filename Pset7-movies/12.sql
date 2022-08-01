SELECT title FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON people.id = stars.person_id
WHERE name LIKE '%Johnny Depp%'
AND title IN (
SELECT title FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON people.id = stars.person_id
WHERE name LIKE '%Helena Bonham Carter%')
;