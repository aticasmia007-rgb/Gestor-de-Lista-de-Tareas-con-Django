from django.urls import path
from . import views
#Se tiene que llamar así la variable para que django lo reconozca
urlpatterns = [
    path("", views.index, name="index"), #vista raiz
    path("/lists/", views.lists, name="lists"), #vista listas
    path('/lists/<int:list_id>/', views.lists_delete,  name = "lists_delete"),
    #path("\lists\tasks", views.tasks, name="tasks"),
    path("/lists/<int:list_id>/tasks/", views.tasks, name="tasks"),
    path("/lists/<int:list_id>/tasks/<int:task_id>/", views.tasks_delete, name="tasks_delete")
]