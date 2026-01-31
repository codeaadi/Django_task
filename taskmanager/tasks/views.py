from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.shortcuts import get_object_or_404


def signup(request):
    form = UserCreationForm()  # ✅ ALWAYS define first

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'tasks/signup.html', {'form': form})


@login_required
def task_list(request):
    tasks=Task.objects.filter(user=request.user)
    return render(request,'tasks/task_list.html',{'tasks':tasks})


@login_required
def task_create(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')

    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_update(request,pk):
    task =get_object_or_404(Task,pk=pk,user=request.user)
    form= TaskForm(instance=task)
    
    if request.method == 'POST':
        form= TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        
        
    return render(request,'tasks/task_form.html',{'form':form})   

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
 