from create_tables import create_tables
from insert_in_tables import insert_in_tables
from select_from_tables import select_from_tables
from export_to_xml import export_to_xml

from http.server import HTTPServer, CGIHTTPRequestHandler

# Создание взаимосвязанных таблиц: Соискатели, Рекрутеры, работодатели. Задание 1, 2
create_tables()

# Заполнение таблиц данными. Задание 3
insert_in_tables()

# Запросы SELECT к таблицам. . Задание 4
select_from_tables()

# Экспорт таблицы Соискатели в XML файл main.xml с помощью библиотеки ElementTree. . Задание 8
export_to_xml()


server_address = ("", 8000)

httpd = HTTPServer(server_address, CGIHTTPRequestHandler)

print("Starting simple_httpd on port: " + str(httpd.server_port))

httpd.serve_forever()
