from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import StudentModelForm
from .models import Student
from django.forms import formset_factory


class IndexView(View):
    def get(self, request):
        form = StudentModelForm()
        context = {
            "form": form
        }

        return render(request, "index.html", context)

    def post(self, request):
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('Student was created')