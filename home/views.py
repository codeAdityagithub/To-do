from django.shortcuts import render, HttpResponse, redirect
from home.models import AllTasks
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model

#password is asdfaggg

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')

    context ={'submit':'not'}
    if request.method == "POST":
        user = request.user
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        if title.strip() != '':
            task = AllTasks(user = user, title = title, desc = desc)
            task.save()
            context ={'submit':'submitted'}
        else:
            context ={'submit':'rejected'}    
    return render(request, "index.html", context)

def tasks(request):
    if request.user.is_anonymous:
        return redirect('/login')

    if request.method == "POST":
        if 'del' in request.POST:
            user = request.user
            index = int(request.POST.get('del')) -1
            AllTasks.objects.filter(user = user)[index].delete()
       
        if 'updateind' in request.POST:
            user = request.user

            print(request.POST['updateval'])
            index = int(request.POST.get('updateind')) -1
            newval = request.POST.get('updateval')
            
            obj = AllTasks.objects.filter(user = user)[index]
            obj.desc = newval
            obj.save()

    if request.user.is_authenticated:
        user = request.user
        allTasks =[]
        for task in AllTasks.objects.filter(user = user):
            temp={'title':task.title, 'desc':task.desc}
            allTasks.append(temp)
        
        
        context = {'allTasks':allTasks}

        return render(request, 'tasks.html', context)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('/')
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutuser(request):

    logout(request)
    return redirect('/login')

def signup(request):
    context = {'userexists':False, 'notmatch':True}
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        usermodel = get_user_model()
        users = usermodel.objects.all()
        for user in users:
            if user.username == username:
                context['userexists'] = True
                return render(request, 'signup.html', context)
        
        if not context['userexists']:
            if password1==password2:
                user = User.objects.create_user(username=username, password=password1)
                if user:
                    print(user)
                return redirect('/login')
            else:
                context['notmatch'] = False
                return render(request, 'signup.html', context)
                
    return render(request, 'signup.html')    