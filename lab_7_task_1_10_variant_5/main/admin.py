from django.contrib import admin
from .models import Recruiter, Employer, Applicant


class RecruiterAdmin(admin.ModelAdmin):
    list_display = ('name', 'successCount')
    list_filter = ('name', 'successCount')


admin.site.register(Recruiter, RecruiterAdmin)


class EmployerAdmin(admin.ModelAdmin):
    list_display = ('name', 'companyName')
    list_filter = ('name', 'companyName')


admin.site.register(Employer, EmployerAdmin)


class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience', 'recruiter', 'employer')
    list_filter = ('name', 'experience', 'recruiter', 'employer')

    def recruiter(self, obj):
        return obj.recruiter

    def employer(self, obj):
        return obj.employer

    recruiter.short_description = 'Рекрутер'
    employer.short_description = 'Работодатель'


admin.site.register(Applicant, ApplicantAdmin)
