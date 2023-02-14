from django.shortcuts import render, redirect
from .models import Teacher, Course, Department
from .forms import *
from django.http import HttpResponse

# Create your views here.


def home(request):
    all_teacher = Teacher.objects.all()
    return render(request, 'home.html', {'teacher': all_teacher})


def remove(request, id):
    var = Teacher.objects.get(id=id)
    var.delete()
    return redirect('home')


def addnew(request):
    varForm = TeacherForm()
    return render(request, "addnew.html", {"TeacherForm": varForm})


def update(request):
    if request.method == "POST":
        tForm = TeacherForm(request.POST)
        if tForm.is_valid():
            tForm.save()
            return redirect(home)
        else:
            return redirect(HttpResponse('Error'))


def edit(request, id):
    match_obj = Teacher.objects.get(id=id)
    tForm = TeacherForm(instance=match_obj)
    return render(request, "edit.html", {"tForm": tForm, "match_obj":match_obj})
