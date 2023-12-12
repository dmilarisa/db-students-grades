SELECT s.group_id, s.name, g.subject_id, g.grade
FROM students s 
JOIN grades g 
WHERE s.group_id = 2 AND g.subject_id = 1
ORDER BY s.name ASC