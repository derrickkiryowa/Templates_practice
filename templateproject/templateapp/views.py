from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from .forms import TaskForm
from .models import Task
from django.urls import reverse

# Create your views here.
tasks = {
  'monday' : ['workhard', 'meditation', 'martial arts spiring'], 'tuesday': 'Go gofy', 'wednesday': 'create' , 'friday'
: 'Soccer'}


def task(request, day):
    to_do = tasks.get(day)
    form = TaskForm()


    return render(request, 'templateapp/base.html', {'data': to_do, 'title':day, 'form': form})


def index(request):
    return HttpResponse('<h1> Hello world</h1>')


def create_task(request):
    tasklist = Task.objects.all()
     
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            details = form.cleaned_data['details']
            no_people = form.cleaned_data['no_people']
            date_created = form.cleaned_data['date_created']
            day_of_week = form.cleaned_data['day_of_week']
            Task.objects.create(name = name, details = details, no_people = no_people, date_created = date_created, day_of_week = day_of_week)
    else:
        form = TaskForm() 
        tasklist = Task.objects.all() #empty instance of form
    return render(request, 'templateapp/base.html', { 'form': form, 'tasklist': tasklist })

def delete_tasks(request, task_id):
    Task.objects.filter(id=task_id).delete()
    redirect_url = reverse('create_task')
    return HttpResponseRedirect(redirect_url)


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            details = form.cleaned_data['details']
            no_people = form.cleaned_data['no_people']
            date_created = form.cleaned_data['date_created']
            day_of_week = form.cleaned_data['day_of_week']
            
            #updating fields in database
            task.name = name
            task.details = details
            task.no_people = no_people
            task.date_created = date_created
            task.day_of_week = day_of_week
            task.save()

            redirect_url = reverse('create_task')
            return HttpResponseRedirect(redirect_url)
        
        #instantiating the form ,were they are able to passin data
    else:
        form = TaskForm(initial={'name': task.name, 'details': task.details, 'no_people': task.no_people, 'date_created': task.date_created, 'day_of_week': task.day_of_week})
        return render(request, 'templateapp/edit_task.html', {'form': form, 'task_id': task_id})




# def task1(request):
#   return HttpResponse('<h1>Tuesday Task: Go shopping</h1>')

# def task2(request):
#   return HttpResponse('<h1>Wednesday Task: Go Gym</h1>')

# def task3(request):
#   return HttpResponse('<h1>Thursday Task: Go Golfy</h1>')


