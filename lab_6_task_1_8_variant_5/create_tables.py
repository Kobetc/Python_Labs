import sqlite3


def create_tables():

    connection = sqlite3.connect('.sqlite3')
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS Recruiter")
    cursor.execute("DROP TABLE IF EXISTS Employer")
    cursor.execute("DROP TABLE IF EXISTS Applicant")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Recruiter (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    successCount INTEGER NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Employer (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    companyName TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Applicant (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    experience INTEGER NULL,
    recruiter_id INTEGER INTEGER NULL,
    employer_id INTEGER INTEGER NULL,

    FOREIGN KEY (recruiter_id) REFERENCES Recruiter(id) ON UPDATE SET NULL,
    FOREIGN KEY (employer_id) REFERENCES Employer(id) ON UPDATE SET NULL
    )
    """)
