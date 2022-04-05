from django import forms

class CreateStudentForm(forms.Form):
    name = forms.CharField(label='Student name', max_length=100)