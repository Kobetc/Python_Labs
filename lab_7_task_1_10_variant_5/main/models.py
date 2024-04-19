from django.db import models


#
# Таблица Рекрутер
#
class Recruiter(models.Model):
    name = models.CharField('Имя', max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name

#
# Таблица Работодатель
#


class Employer(models.Model):
    name = models.CharField('Имя', max_length=50, null=False, unique=True)
    companyName = models.CharField('Имя компании', max_length=255, null=False)

    def __str__(self):
        return f"{self.name} - {self.companyName}"

#
# Таблица Соискатель
#


class Applicant(models.Model):
    name = models.CharField('Имя', max_length=50, null=False, unique=True)
    experience = models.IntegerField('Стаж работы', null=False, default=0)
    id_recruiter = models.IntegerField('id рекрутера', null=True)
    id_employer = models.IntegerField('id работодателя', null=True)

    def __str__(self):
        return self.name
