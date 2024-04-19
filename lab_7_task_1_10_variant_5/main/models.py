from django.db import models


#
# Таблица Рекрутер
#
class Recruiter(models.Model):
    name = models.CharField('Имя', max_length=50, null=False, unique=True)
    successCount = models.IntegerField(
        'Число успешных устройств', null=False, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рекрутер"
        verbose_name_plural = "Рекрутеры"

#
# Таблица Работодатель
#


class Employer(models.Model):
    name = models.CharField('Имя', max_length=50, null=False, unique=True)
    companyName = models.CharField('Имя компании', max_length=255, null=False)

    def __str__(self):
        return f"{self.name} - {self.companyName}"

    class Meta:
        verbose_name = "Работодатель"
        verbose_name_plural = "Работодатели"

#
# Таблица Соискатель
#


class Applicant(models.Model):
    name = models.CharField('Имя', max_length=50, null=False, unique=True)
    experience = models.IntegerField('Стаж работы', null=False, default=0)
    recruiter = models.ForeignKey(
        Recruiter, on_delete=models.SET_NULL, null=True, blank=True)
    employer = models.ForeignKey(
        Employer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Соискатель"
        verbose_name_plural = "Соискатели"
