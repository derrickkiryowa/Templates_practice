from django import forms 

class TaskForm(forms.Form):
    name = forms.CharField(max_length=100)
    details = forms.CharField(max_length=1000)
    no_people = forms.IntegerField()
    date_created = forms.DateTimeField()
    day_of_week = forms.CharField(max_length= 100)