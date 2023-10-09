from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.shortcuts import get_object_or_404

# Create your views here.

from .models import Profile,Task

@login_required(login_url='login_page')
def dashboard(request):
    user = request.user
    tasks= Task.objects.filter(user=user)
    return render(request,'dashboard.html',{'tasks':tasks})
@login_required(login_url='login_page')
def edit_task(request,task_id):
    if request.method=='POST':
        task = get_object_or_404(Task,pk=task_id)
        name=request.POST.get('name')
        description=request.POST.get('description')
        priority=request.POST.get('priority')
        due_date=request.POST.get('due_date')
        status=request.POST.get('status')
        task.task_name=name
        task.task_description=description
        task.task_priority =priority
        task.task_due_date =due_date
        if status=='true':
            task.task_completed = True
        elif status=='false':
            task.task_completed = False   
        task.save()
        return redirect('dashboard')     
    return redirect('dashboard')

@login_required(login_url='login_page')
def delete_task(request,task_id):
    task = get_object_or_404(Task,pk=task_id)
    task.delete()
    return redirect('dashboard')     
    

@login_required(login_url='login_page')
def add_task(request):
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        priority=request.POST.get('priority')
        due_date=request.POST.get('due_date')
        Task.objects.create(user=request.user,task_name=name,task_description=description,task_priority =priority,task_due_date =due_date)
        return redirect('dashboard')     
    return redirect('dashboard')

def login_page(request):
    return render(request,'login.html',{'title':'login page'})
def register_page(request):
    return render(request,'register.html',{'title':'register page'})
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            msg='Username and Password does not exists'
            return render(request,'login.html',{'msg':msg})
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        name=request.POST.get('name')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirmpassword')
        profile_pic=request.FILES.get('profile_pic')
        if request.FILES:
            if password==confirm_password:
                if Profile.objects.filter(username=username).exists():
                    msg1='Username already taken'
                    return render(request,'register.html',{'msg1':msg1,'name':'name'})
                else:
                    user=Profile.objects.create_user(username=username,password=password,photo=profile_pic,name=name)
                    msg2='Successfully created'
                    return render(request,'login.html',{'msg2':msg2,'username':username})
            else:
                msg3='Password does not match'
                return render(request,'register.html',{'msg3':msg3,'username':username,'name':name})
        else:
            msg4='Add a profile pic'
            return render(request,'register.html',{'msg4':msg4,'username':username,'name':name})
    else:
        return render(request,'register.html')
    
@login_required(login_url='login_page')
def logout(request):
    auth.logout(request)
    return redirect('login_page')    