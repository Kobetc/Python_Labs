import sqlite3


def delete_in_table_applicants():

    connection = sqlite3.connect('.sqlite3')
    cursor = connection.cursor()

    cursor.execute("DELETE FROM Applicant")

    connection.commit()
