from sqlite3 import Error

from connect import create_connection, database


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


if __name__ == '__main__':
    sql_create_students = '''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50),
            group_id INTEGER,
            FOREIGN KEY (group_id) REFERENCES groups(id)
        );
    '''

    sql_create_groups = '''
        CREATE TABLE IF NOT EXISTS groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50)
        );
    '''

    sql_create_teachers = '''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50)
        );
    '''

    sql_create_subjects = '''
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            teacher_id INTEGER,
            FOREIGN KEY (teacher_id) REFERENCES teachers(id)
        );
    '''

    sql_create_grades = '''
        CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject_id INTEGER,
        grade INTEGER,
        date_received DATE,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (subject_id) REFERENCES subjects(id)
        );
    '''

    with create_connection(database) as conn:
        if conn is not None:
            create_table(conn, sql_create_students)
            create_table(conn, sql_create_groups)
            create_table(conn, sql_create_teachers)
            create_table(conn, sql_create_subjects)
            create_table(conn, sql_create_grades)
        else:
            print("Error. Cannot create the database connection")

