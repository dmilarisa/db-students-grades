SELECT s.name, s.group_id as group_id 
FROM students s 
WHERE s.group_id = 2
ORDER BY s.name ASC