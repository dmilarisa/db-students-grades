SELECT  g.name as group_n, s.name as student, sub.name as subject, gr.date_received as last_date
FROM groups g
JOIN students s ON s.group_id = g.id
JOIN grades gr ON gr.student_id = s.id 
JOIN subjects sub ON sub.id = gr.subject_id
WHERE gr.date_received = 
	(SELECT MAX(gr.date_received) 
	 FROM grades gr 
	 WHERE gr.student_id IN 
	 	(SELECT s.id 
	 	 FROM students s 
	 	 WHERE s.group_id = 3)) 
	AND sub.id = 3 

