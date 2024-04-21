#!/usr/bin/python

import sys
import codecs
import sqlite3

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

connection = sqlite3.connect('.sqlite3')
cursor = connection.cursor()
cursor = connection.execute(
    """
        SELECT 
            id, 
            name, 
            experience, 
            (SELECT name FROM Employer WHERE Applicant.employer_id  = Employer.id), 
            (SELECT companyName FROM Employer WHERE Applicant.employer_id  = Employer.id), 
            (SELECT name FROM Recruiter WHERE Applicant.recruiter_id  = Recruiter.id) 
        FROM Applicant
    """
)

print('''
<!DOCTYPE html>
<html lang="ru">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
        rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
        crossorigin="anonymous">
    <title>Кадровое агентство - Просмотр таблицы Соискатели</title>
</head>

<body>
    <div class="container-fluid p-3" style="min-height: 100vh">
        <header>
            <div class="d-flex flex-column flex-md-row align-items-center p-3 mb-4 border-bottom">
                <a href="/" class="d-flex align-items-center link-body-emphasis text-decoration-none">
                    <span class="fs-4">Кадровое агентство</span>
                </a>

                <nav class="d-inline-flex mt-2 mt-md-0 ms-md-auto">
                    <a class="me-3 py-2 link-body-emphasis text-decoration-none" href="/">Главная</a>
                    <a class="me-3 py-2 link-body-emphasis text-decoration-none" href="/cgi-bin/list.py">Список</a>
                    <a class="me-3 py-2 link-body-emphasis text-decoration-none" href="/cgi-bin/list.py">Добавить</a>
                </nav>

            </div>
        </header>
            <main style="min-height: 55vh">
                <div class="container p-3" style="min-height: 100vh">
                    <div class="row p-3">
                    <div class="col p-3">
                        <h3>Просмотр таблицы Соискатели</h3>
                    </div>
                </div>
        
                <div class="row p-3">
                    <div class="col">
                        <table class="table">
                            <thead>
                                <tr>
                                <th scope="col">#</th>
                                <th scope="col">Имя</th>
                                <th scope="col">Опыт работы</th>
                                <th scope="col">Работодатель</th>
                                <th scope="col">Компания Работодателя</th>
                                <th scope="col">Рекрутер</th>
                                </tr>
                            </thead>
                            <tbody>
''')


for row in cursor.fetchall():
    print(f"<TR>",
          f"<th scope='row'> {row[0]}</th>",
          f" <TD> {row[1]} </TD> ",
          f" <TD> {row[2]} </TD> ",
          f" <TD> {'---' if row[3] == None else row[3]} </TD> ",
          f" <TD> {'---' if row[4] == None else row[4]} </TD> ",
          f" <TD> {'---' if row[5] == None else row[5]} </TD>",
          f"</TR>")


print('''
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </main>
        <footer class="pt-4 my-md-5 pt-md-5 p-3 border-top">
            <div class="row">
                <div class="col-12 col-md">
                    <small class="d-block mb-3 text-body-secondary">© 2024</small>
                </div>
                <div class="col-6 col-md" style="text-align: end;">
                    <h5>Разделы сайта</h5>
                    <ul class="list-unstyled text-small">
                        <li class="mb-1"><a class="link-secondary text-decoration-none" href="/">Главная</a></li>
                        <li class="mb-1"><a class="link-secondary text-decoration-none" href="/cgi-bin/list.py">Список</a></li>
                        <li class="mb-1"><a class="link-secondary text-decoration-none" href="/cgi-bin/list.py">Добавить</a></li>
                    </ul>
                </div>
            </div>
        </footer>
    </div>
</body>
</html>
''')

connection.close()
