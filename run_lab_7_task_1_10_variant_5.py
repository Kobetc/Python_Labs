import os
import webbrowser


webbrowser.open_new('http://127.0.0.1:8000/')
os.chdir("lab_7_task_1_10_variant_5")
os.system("python manage.py runserver")
