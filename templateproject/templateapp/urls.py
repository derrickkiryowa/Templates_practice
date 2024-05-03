from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.create_task, name = 'create_task'), #route used to process the form data.
    path('delete/<int:task_id>', views.delete_tasks, name = 'delete_task'),
    path('update/<int:task_id>', views.edit_task, name = 'edit_task'),
]
