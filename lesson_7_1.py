import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_student(conn, student):
    """
    Create a new student into the students table
    :param conn:
    :param student:
    :return: student id
    """
    sql = ''' INSERT INTO students(full_name, mark, age, hobby, birth_date)
              VALUES(?,?,?,?,?); '''
    cur = conn.cursor()
    cur.execute(sql, student)
    conn.commit()
    return cur.lastrowid


def update_student_mark(conn, student):
    """
    update mark of a student
    :param conn:
    :param student:
    :return:
    """
    sql = ''' UPDATE students SET mark = ? WHERE id = ?; '''
    cur = conn.cursor()
    cur.execute(sql, student)
    conn.commit()


def delete_student(conn, id):
    """
    Delete a student by student id
    :param conn:  Connection to the SQLite database
    :param id: id of the student
    :return:
    """
    sql = ''' DELETE FROM students WHERE id = ?; '''
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def select_all_students(conn):
    """
    Query all rows in the students table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_students_by_mark(conn, mark):
    """
    Query students by mark
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE mark >= ?", (mark,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


database = r'example.db'
sql_create_students_table = ''' 
CREATE TABLE students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR (200) NOT NULL,
mark DOUBLE (5, 2) NOT NULL DEFAULT 0.0,
age INTEGER NOT NULL,
hobby TEXT DEFAULT NULL,
birth_date DATE NOT NULL
); '''

conn = create_connection(database)

# create tables
if conn is not None:
    # create projects table
    # create_table(conn, sql_create_students_table)
    print("Connected successfully!")

    # create_student(conn, ("Mark Daniels", 77.12, 22, "Football", "1999-01-02"))
    # create_student(conn, ("Alex Brilliant", 77.12, 35, None, "1989-12-31"))
    # create_student(conn, ("Diana Julls", 99.3, 15, "Tennis", "2005-01-22"))
    # create_student(conn, ("Michael Corse", 100.0, 19, "Watching movies", "2001-01-12"))

    # update_student_mark(conn, (99.2, 12))

    # delete_student(conn, 1)

    # select_all_students(conn)

    select_students_by_mark(conn, 90.0)
    conn.close()
else:
    print("Error! cannot create the database connection.")
