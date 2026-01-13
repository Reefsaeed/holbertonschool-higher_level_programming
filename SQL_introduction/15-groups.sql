-- List number of records with the same score
-- Display score and count (as number), sorted by count descending

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
