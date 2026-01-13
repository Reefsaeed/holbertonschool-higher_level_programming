-- List records from second_table where name is not NULL
-- Display score then name, ordered by score descending

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
