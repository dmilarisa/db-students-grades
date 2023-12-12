SELECT s.name, t.name, AVG(g.grade) as avg_grade
FROM students s 
JOIN grades g ON g.student_id = s.id 
JOIN subjects sub ON sub.id = g.subject_id
JOIN teachers t ON t.id =sub.teacher_id 
WHERE t.id = 4 AND s.id = 5
GROUP BY s.id 

