
from django.utils import timezone
from django.db import models

# Create your models here.
class TaskList(models.Model):
    #id= models.IntegerField() #Es importante que siempre lleve paréntesis aunque sean vacios!
    name= models.CharField(max_length=200)
    created_at= models.DateTimeField(default = timezone.now) #me planteo a cambiarlo a auto

class Task(models.Model):
    #id= models.IntegerChoices() --> Se hace automatico en django
    title= models.CharField(max_length=200)
    completed= models.BooleanField(default=False) #Le pongo un default, cuando no esté creada se queda en falso
    created_at= models.DateTimeField(default = timezone.now) #Puedo poner auto_now_add= True pero no deja editar el campo// o el timezone.now SIN PARENTESIS que lo modifica
    task_list = models.ForeignKey(TaskList,on_delete= models.CASCADE) # Siempre pasarle a la FK a qué se conecta y como actualizarlo