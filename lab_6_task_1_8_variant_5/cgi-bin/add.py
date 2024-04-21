#!/usr/bin/python

from cgi import FieldStorage
import sys
import codecs
import sqlite3


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

connection = sqlite3.connect('.sqlite3')
cursor = connection.cursor()


form = FieldStorage()


name = form.getvalue('name')
experience = form.getvalue('experience')
recruiter_id = form.getvalue('recruiter_id')
employer_id = form.getvalue('employer_id')

if name != None:

    cursor.execute("INSERT INTO Applicant VALUES(?, ?, ?, ?, ?)",
                   (None, name, experience, recruiter_id, employer_id))
    connection.commit()

    print('''
        <!DOCTYPE html>
            <head>
                <meta http-equiv="refresh" content="0;url='/cgi-bin/list.py'" />'
            </head>
        </html>
    ''')


cursor = connection.execute("SELECT * FROM Employer")
employers = cursor.fetchall()

cursor = connection.execute("SELECT * FROM Recruiter")
recruiters = cursor.fetchall()

print('''
<!DOCTYPE html>
<html lang="ru">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
        rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
        crossorigin="anonymous">
    <title>Кадровое агентство - Добавление записи в таблицу Соискатели</title>
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
                    <a class="me-3 py-2 link-body-emphasis text-decoration-none" href="/cgi-bin/add.py">Добавить</a>
                </nav>

            </div>
        </header>
            <main style="min-height: 55vh">
                <div class="container p-3" style="min-height: 100vh">
                    <div class="row p-3">
                    <div class="col p-3">
                        <h3>Добавление записи в таблицу Соискатели</h3>
                    </div>
                </div>
        
                <div class="row p-3">
                    <div class="col">

''')

print('''
                        <form action="add.py" method="post" class="needs-validation">

                            <div class="input-group flex-nowrap mb-3">
                                <span class="input-group-text" id="name">Имя</span>
                                <input type="text" class="form-control" name="name" id="name" required>
                            </div>

                            <div class="input-group flex-nowrap mb-3">
                                <span class="input-group-text" id="experience">Стаж</span>
                                <input type="number" class="form-control" name="experience" id="experience" step="1" min="0" max="99"
                                    required>
                            </div>

                            <div class="input-group flex-nowrap mb-3">
                                <span class="input-group-text" id="recruiter_id">Рекрутер</span>
                                <select class="form-select" aria-label="Default select example" name="recruiter_id" id="recruiter_id">
                                    <option value=""></option>
''')

for recruiter in recruiters:
    print(f"<option value='{recruiter[0]}'>{recruiter[1]}</option>")

print('''     
                                </select>
                            </div>

                            <div class="input-group flex-nowrap mb-3">
                                <span class="input-group-text" id="employer_id">Работодатель</span>
                                <select class="form-select" aria-label="Default select example" name="employer_id" id="employer_id">
                                    <option value=""></option>
''')

for employer in employers:
    print(f"<option value='{employer[0]}'>{employer[1]}</option>")

print('''                        
                                </select>
                            </div>

                            <div class="input-group flex-nowrap mb-3">
                                <button type="submit" class="btn btn-primary mb-3">Создать позицию</button>
                            </div>
                        </form>
''')


print('''

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
                        <li class="mb-1"><a class="link-secondary text-decoration-none" href="/cgi-bin/add.py">Добавить</a></li>
                    </ul>
                </div>
            </div>
        </footer>
    </div>
</body>
</html>
''')

connection.close()
