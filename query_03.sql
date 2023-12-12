SELECT groups.id, groups.name, grades.subject_id, AVG(grades.grade)
FROM groups 
JOIN students ON students.group_id = groups.id 
JOIN grades on grades.student_id = students.id
WHERE grades.subject_id = 2
GROUP BY groups.id 

