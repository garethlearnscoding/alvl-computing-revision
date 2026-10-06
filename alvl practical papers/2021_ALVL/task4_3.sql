--Task 4.3 SQL
SELECT competitor.name, scores.score, AVG(scores.score)
FROM scores
INNER JOIN competitor ON scores.id = competitor.id
GROUP BY competitor.name
ORDER BY AVG(scores.score) ASC;