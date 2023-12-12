SELECT t.name,  s.name, AVG(g.grade) as avg_grade
FROM teachers t 
JOIN subjects s ON s.teacher_id = t.id 
JOIN grades g ON g.subject_id = s.id 
WHERE t.id = 4
GROUP BY s.id 
