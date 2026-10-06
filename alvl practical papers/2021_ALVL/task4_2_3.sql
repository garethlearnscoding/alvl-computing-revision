--Task 4.2 SQL
SELECT competitor.name, scores.score
FROM scores
INNER JOIN competitor ON scores.id = competitor.id
WHERE scores.round = 3
ORDER BY scores.score DESC;