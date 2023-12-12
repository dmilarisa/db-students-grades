from sqlite3 import Error
from connect import create_connection, database
from faker import Faker
import random
from datetime import datetime, timedelta


def insert_data(conn, sql_expression, data_set):
    cur = conn.cursor()
    try:
        cur.execute(sql_expression, data_set)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()


if __name__ == '__main__':

    group_names = ['Group A', 'Group B', 'Group C']
    subject_names = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'English', 'Computer Science', 'Art']
    fake = Faker()
    teacher_names = [fake.name() for _ in range(5)]

    with create_connection(database) as conn:
        sql_groups = """
            INSERT INTO groups (name) VALUES (?)
        """
        for group_name in group_names:
            insert_data(conn, sql_groups, (group_name,))

        sql_students = """
            INSERT INTO students (name, group_id) VALUES (?, ?)
        """
        for _ in range(50):
            student_name = fake.name()
            group_id = random.randint(1, len(group_names))
            insert_data(conn, sql_students, (student_name, group_id))

        sql_teachers = """
            INSERT INTO teachers (name) VALUES (?)
        """
        for teacher_name in teacher_names:
            insert_data(conn, sql_teachers, (teacher_name,))

        sql_subjects = """
            INSERT INTO subjects (name, teacher_id) VALUES (?, ?)
        """
        for subject_name in subject_names:
            teacher_id = random.randint(1, len(teacher_names))
            insert_data(conn, sql_subjects, (subject_name, teacher_id))

        sql_grades = """
            INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)
        """
        for student_id in range(1, 51):
            for subject_id in range(1, len(subject_names) + 1):
                grade = random.randint(60, 100)
                date_received = fake.date_between(start_date='-1y', end_date='today')
                insert_data(conn, sql_grades, (student_id, subject_id, grade, date_received))
