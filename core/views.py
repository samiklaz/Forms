from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import CreateStudentForm
from .models import Student
from django.forms import formset_factory

class IndexView(View):
    def get(self, request):
        StudentFormset = formset_factory(CreateStudentForm, extra=3)
        student_formset = StudentFormset(initial = [
            {'name': 'Asuquo Samuel'}
        ])

        context = {
            "formset": student_formset
        }
        return render(request, "index.html", context)

    def post(self, request):
        form = CreateStudentForm(request.POST)

        if form.is_valid():
            student_name = form.cleaned_data['name']
            student = Student.objects.create(name=student_name)
            student.save()
            return HttpResponse("Student was created with name " + student_name)

        context = {
            "form": form
        }
        return render(request, "index.html", context)