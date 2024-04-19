from django.shortcuts import render
from .models import Applicant, Recruiter, Employer


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def list(request):
    if request.method == "POST":
        editId = request.POST.get("editId")
        deleteId = request.POST.get("deleteId")

        print(editId, deleteId)

    applicants = Applicant.objects.all()

    return render(request, 'main/list.html', {'applicants': applicants})


def add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        experience = request.POST.get("experience")

        recruiter = request.POST.get("recruiter")
        employer = request.POST.get("employer")

        experience = int(experience) if len(experience) > 0 else None
        recruiter = int(recruiter) if len(recruiter) > 0 else None
        employer = int(employer) if len(employer) > 0 else None

        newApplicant = Applicant.objects.create(
            name=name, experience=experience, recruiter=recruiter, employer=employer)

        newApplicant.save()

    recruiters = Recruiter.objects.all()
    employers = Employer.objects.all()

    return render(request, 'main/add.html', {'recruiters': recruiters, 'employers': employers})
