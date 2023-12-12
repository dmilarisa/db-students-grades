SELECT s.id, s.name, g.subject_id,  AVG(g.grade) avg_grade
FROM students s 
JOIN grades as g ON s.id = g.student_id 
WHERE g.subject_id = 1
GROUP BY student_id 
ORDER BY avg_grade DESC
LIMIT 1