import sqlite3


def select_from_tables():

    connection = sqlite3.connect('.sqlite3')
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM Applicant WHERE experience > 0")
    print(cursor.fetchall())

    cursor.execute(
        "SELECT * FROM Applicant WHERE employer_id NOT NULL")
    print(cursor.fetchall())

    cursor.execute(
        "SELECT name, (SELECT companyName FROM Employer WHERE Applicant.employer_id  = Employer.id) FROM Applicant WHERE employer_id IS NOT NULL")
    print(cursor.fetchall())
