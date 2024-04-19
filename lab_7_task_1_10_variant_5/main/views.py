from django.shortcuts import render, redirect
from .models import Applicant, Recruiter, Employer


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def list(request):
    if request.method == "POST":
        viewId = request.POST.get("viewId")
        editId = request.POST.get("editId")
        deleteId = request.POST.get("deleteId")

        if viewId != None:
            return redirect('view', id=viewId)

        if editId != None:
            return redirect('edit', id=editId)

        if deleteId != None:
            person = Applicant.objects.get(id=int(deleteId))
            person.delete()

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


def edit(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        experience = request.POST.get("experience")

        recruiter = request.POST.get("recruiter")
        employer = request.POST.get("employer")

        experience = int(experience) if len(experience) > 0 else None
        recruiter = int(recruiter) if len(recruiter) > 0 else None
        employer = int(employer) if len(employer) > 0 else None

        Applicant.objects.filter(id=int(id)).update(name=name,
                                                    experience=experience, recruiter=recruiter, employer=employer)

        return redirect("list")

    applicant = Applicant.objects.get(id=int(id))
    recruiter = None
    employer = None

    if applicant.recruiter != None:
        recruiter = Recruiter.objects.get(id=int(applicant.recruiter.id))

    if applicant.employer != None:
        employer = Employer.objects.get(id=int(applicant.employer.id))

    recruiters = Recruiter.objects.all()
    employers = Employer.objects.all()

    return render(request, 'main/edit.html', {'applicant': applicant, 'recruiter': recruiter, 'employer': employer, 'recruiters': recruiters, 'employers': employers})


def view(request, id):

    applicant = Applicant.objects.get(id=int(id))

    return render(request, 'main/view.html', {'applicant': applicant})
