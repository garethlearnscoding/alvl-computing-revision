--Task 4.4 SQL
SELECT competitor.name, SUM(scores.score), SUM(scores.score)>250
FROM scores
INNER JOIN competitor ON scores.id = competitor.id
GROUP BY competitor.name
ORDER BY SUM(scores.score) DESC;