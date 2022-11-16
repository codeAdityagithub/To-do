from django.shortcuts import render, HttpResponse, redirect
from home.models import Tasks
# Create your views here.
def index(request):
    context ={'submit':'not'}
    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        if title.strip() != '':
            task = Tasks(title = title, desc = desc)
            task.save()
            context ={'submit':'submitted'}
        else:
            context ={'submit':'rejected'}    
    return render(request, "index.html", context)

def tasks(request):
   
    if request.method == "POST":
        if 'del' in request.POST:
            index = int(request.POST.get('del')) -1
            Tasks.objects.all()[index].delete()
       
        if 'updateind' in request.POST:
            print(request.POST['updateval'])
            index = int(request.POST.get('updateind')) -1
            newval = request.POST.get('updateval')
            
            obj = Tasks.objects.all()[index]
            obj.desc = newval
            obj.save()


    allTasks =[]
    for task in Tasks.objects.all():
        temp={'title':task.title, 'desc':task.desc}
        allTasks.append(temp)
    
    
    context = {'allTasks':allTasks}

    return render(request, 'tasks.html', context)

