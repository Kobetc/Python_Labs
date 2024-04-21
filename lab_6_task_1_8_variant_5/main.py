from http.server import HTTPServer, CGIHTTPRequestHandler

import sqlite3

connection = sqlite3.connect('.sqlite3')
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS Recruiter")
cursor.execute("DROP TABLE IF EXISTS Employer")
cursor.execute("DROP TABLE IF EXISTS Applicant")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Recruiter (
id INTEGER PRIMARY KEY,
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

recruiters = [
    (1, "Тестовый Рекрутер 1", 1),
    (2, "Тестовый Рекрутер 2", 10),
    (3, "Тестовый Рекрутер 3", 45),
    (4, "Тестовый Рекрутер 4", 11),
    (5, "Тестовый Рекрутер 5", 23),
    (6, "Тестовый Рекрутер 6", 15),
]

employers = [
    (1, "Тестовый Работодатель 1", "Тестовая Компания 1"),
    (2, "Тестовый Работодатель 2", "Тестовая Компания 2"),
    (3, "Тестовый Работодатель 3", "Тестовая Компания 3"),
]

applicants = [
    (1, "Тестовый Соискатель 1", 0, None, None),
    (2, "Тестовый Соискатель 2", 10, 1, None),
    (3, "Тестовый Соискатель 3", 15, None, None),
    (4, "Тестовый Соискатель 4", 0, None, None),
    (5, "Тестовый Соискатель 5", 10, 3, 2),
    (6, "Тестовый Соискатель 6", 15, None, None),
]

cursor.executemany("INSERT INTO Recruiter VALUES(?, ?, ?)", recruiters)
cursor.executemany("INSERT INTO Employer VALUES(?, ?, ?)", employers)
cursor.executemany("INSERT INTO Applicant VALUES(?, ?, ?, ?, ?)", applicants)

connection.commit()

server_address = ("", 8000)

httpd = HTTPServer(server_address, CGIHTTPRequestHandler)

print("Starting simple_httpd on port: " + str(httpd.server_port))

httpd.serve_forever()
