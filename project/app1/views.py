from . models import Task
from django.contrib.auth import logout
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        
        if password != cpassword:
            messages.error(request, "Passwords do not match. Please retry.")
            return redirect("")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("")
        
        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.save()       
        return redirect("login")
    
    else:
        messages.info(request, "Please sign up.")
        
    return render(request, "signup.html")



def log(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Use the imported login function
            return redirect("index")  # Redirect to a success page.
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "login.html")


def index(request):
    tasks = Task.objects.all()  # Retrieve all tasks from the database
    return render(request, 'index.html', {'tasks': tasks})

def logout_view(request):
    logout(request)
    return redirect('login')

def add_task(request):
    if request.method == 'POST':
        task_name = request.POST['task_name']
        description = request.POST['description']
        status = request.POST['status']
        Task.objects.create(task_name=task_name, description=description, status=status)
        return redirect('index')
    return render(request,'add_task.html')

def view_tasks(request):
    status_filter = request.GET.get('status')
    if status_filter:
        tasks = Task.objects.filter(status=status_filter)
    else:
        tasks = Task.objects.all()
    return render(request,'view_tasks.html', {'tasks': tasks})
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.task_name = request.POST['task_name']
        task.description = request.POST['description']
        task.status = request.POST['status']
        task.save()
        return redirect('index')
    return render(request, 'edit_task.html', {'task': task})

