SELECT s.name, s.id, AVG(g.grade) AS avg_grade 
FROM students s 
LEFT JOIN grades as g ON s.id = g.student_id 
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 5
