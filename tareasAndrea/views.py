from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
# from django.template import loader
from .models import TaskList, Task
# Create your views here.

def index(request):
    #template = loader.get_template("index.html")
    db_data= TaskList.objects.all() #Nos devuelve un array de los registros de esa tabla
    context={"db_data": db_data} #datos para poder mostrarlos en pantalla
    #return HttpResponse(template.render(context, request))
    return render(request, "index.html", context)

######################LISTAS###########################################3
def lists(request):
    if request.method=="POST": #Para saber si es datos del formulario
        formLista = request.POST.get("nombreLista") #Esto es el name del formulario
        print("Probando" + formLista) #estaba intentando acceder como si fuese un dic
        if formLista:
            TaskList.objects.create(name=formLista) #para guardar en la bd
        return redirect("/lists/") #Que vuelva a lists, pero con una lista más/// Evita duplicados
    #template = loader.get_template("index.html")
    db_data_taskList= TaskList.objects.all() #Nos devuelve un array de los registros de esa tabla
    context={"db_data_taskList": db_data_taskList} #datos para poder mostrarlos en pantalla
    #return HttpResponse(template.render(context, request))
    return render(request, "listas.html", context)

def lists_delete(request, list_id):
    borrandoLista= get_object_or_404(TaskList,pk=list_id) #Al ser el id, es mejor usar PK, primary key. Viene toda la f de shortcuts, le pasas (bd, id)
    if request.method=="POST":
        borrandoLista.delete() #get_object_ir_404 es para controlar si meten un id que no existe
        return redirect("/lists/")
    return render(request, "listas_borrar.html", context={"borrandoLista": borrandoLista}) #al contexto hay que pasar diccionarios!

#######################TASKS#########################################################
def tasks(request, list_id):
    lista_corresponde= get_object_or_404(TaskList, pk=list_id) #Lista a la que pertenece
    if request.method=="POST":
        formTask=request.POST.get("tituloTarea")
        if formTask:
            Task.objects.create(title= formTask, task_list=lista_corresponde) #asi conecto con FK
        return redirect(f"/lists/{list_id}/tasks/") #si le paso el id <> no funciona, eso es para las urls
    db_data_task= Task.objects.filter(task_list=lista_corresponde) #coge solo los que tengan el atr tasklist = listid pasado
    context={"lista": lista_corresponde, "tareas": db_data_task} 
    return render(request, "tareas.html", context)

def tasks_delete(request, list_id, task_id): #sigo la misma lógica que list delete
    borrando_estadoTask= get_object_or_404(Task,pk=task_id) #Al ser el id, es mejor usar PK, primary key. Viene toda la f de shortcuts, le pasas (bd, id)
    if request.method=="POST":
        if "borrar" in request.POST: #si es el boton borrar y se busca en el diccionario POST
            
            borrando_estadoTask.delete() 
            return redirect(f"/lists/{list_id}/tasks/")
        elif "cambiarEstado" in request.POST:
            borrando_estadoTask.completed= not borrando_estadoTask.completed #Si tocan al boton, cambia de estado. TRUE FALSE, no más...
            borrando_estadoTask.save()
            return redirect(f"/lists/{list_id}/tasks/")
    return render(request, "tareas_borrar.html", context={"borrando_estadoTask": borrando_estadoTask}) #al contexto hay que pasar diccionarios!

#MËTODO PATCH -->  "FALSO" Esto lo subo arriba, para hacer menos codigo


# def tasks_estado(request, list_id, task_id): #sigo la misma lógica que list delete
#     EstadoTask= get_object_or_404(Task,pk=task_id) #Al ser el id, es mejor usar PK, primary key. Viene toda la f de shortcuts, le pasas (bd, id)
#     if request.method=="POST":
#         EstadoTask.completed= not EstadoTask.completed #Si tocan al boton, cambia de estado. TRUE FALSE, no más...
#         EstadoTask.save()
#         return redirect(f"/lists/{list_id}/tasks/")
    
#     return render(request, "tareas_borrar.html", context={"EstadoTask": EstadoTask}) #al contexto hay que pasar diccionarios!


