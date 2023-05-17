from seiri.models import Task, CompletedTasks
from django.http import HttpResponseRedirect
from seiri.user_form import LoginForm, RegisterForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect


User = get_user_model()


@csrf_exempt
@requires_csrf_token
def register_usr(request):
    form_usr = RegisterForm(request.POST or None)
    if form_usr.is_valid():
        username = form_usr.cleaned_data.get("username")
        email = form_usr.cleaned_data.get("email")
        password = form_usr.cleaned_data.get("password1")
        password2 = form_usr.cleaned_data.get("password2")
        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None
        if user != None:
            login(request, user)
            messages.success(request, f'Welcome, {user.get_username()}!')
            return HttpResponseRedirect("show_tasks")
        else:
            request.session['register_error'] = 1
    return render(request, "auth-register.html", {"form_usr": form_usr})


@csrf_exempt
@requires_csrf_token
def login_usr(request):
    login_form = LoginForm(request.POST or None)

    if login_form.is_valid():

        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        usr = authenticate(request, username=username, password=password)

        if usr != None:
            login(request, usr)
            messages.success(request, f'Welcome, {usr.get_username()}!')
            return HttpResponseRedirect("show_tasks")
        else:
            messages.error(request, 'Invalid user or password!')
            request.session['invalid_user'] = 1
    return render(request, "auth-login.html", {"login_form": login_form})




@login_required()
def logout_usr(request):
    logout(request)
    return HttpResponseRedirect('home')

# informações de perfil
@csrf_exempt
@requires_csrf_token
def usr_profile(request):
    if request.method == 'GET':
        return render(request, 'profile.html')



# alterar senha de user_owner_task
def change_pswd(request):
    pass

# homepage
@csrf_exempt
@requires_csrf_token
def home(request):
    return render(request, 'landingpage.html')

# pagina_principal
@csrf_exempt
@requires_csrf_token
@login_required()
def show_tasks(request):
    task_list = Task.objects.all().filter(user_owner_task=request.user).order_by('date_task')
    return render(request, 'tasks.html', {"tasks": task_list})

# pagina_principal
@csrf_exempt
@requires_csrf_token
@login_required()
def show_tasks_completed(request):
    completed_task = CompletedTasks.objects.all().filter(user_owner_task=request.user).order_by('date_task')
    return render(request, 'completed-tasks.html', {"completed_task": completed_task})


@csrf_exempt
@requires_csrf_token
@login_required()
def add(request):
    if request.method == "POST":
        if request.POST.get('task') \
                and request.POST.get('description') \
                and request.POST.get('date_task') \
                or request.POST.get('priority_level'):
            task = Task()
            task.task = request.POST.get('task')
            task.description = request.POST.get('description')
            task.date_task = request.POST.get('date_task')
            task.priority_level = request.POST.get('priority_level')
            task.user_owner_task = request.user
            task.save()

            messages.success(request, 'Task added with success!')
            
            return HttpResponseRedirect('show_tasks')
    else:
        return render(request, 'md-add-task.html')


# Visualizar task individualmente
@csrf_exempt
@requires_csrf_token
@login_required()
def task(request, task_ID):
    task = Task.objects.get(id=task_ID)
    if task != None:
        return render(request, "md-update-task.html", {'task': task})
    

@csrf_exempt
@requires_csrf_token
@login_required()
def completed_task(request, task_ID):
    c_task = CompletedTasks.objects.get(id=task_ID)
    if c_task != None:
        return render(request, "md-update-task.html", {'c_task': c_task})


@csrf_exempt
@requires_csrf_token
@login_required()
def update_task(request):
    if request.method == "POST":
        task = Task.objects.get(id=request.POST.get('id'))
        if task != None:
            task.task = request.POST.get('task')
            task.description = request.POST.get('description')
            task.date_task = request.POST.get('date_task')
            task.priority_level = request.POST.get('priority_level')
            task.save()
            messages.success(request, 'Task updated successfully!')
            return HttpResponseRedirect('show_tasks')


@csrf_exempt
@requires_csrf_token
@login_required()
def delete_task(request, task_ID):
    task = Task.objects.get(id=task_ID)
    task.delete()
    messages.success(request, 'Task removed successfully!')
    return redirect('show_tasks')

# Remover task
@csrf_exempt
@requires_csrf_token
@login_required()
def delete_task_completed(request, task_ID):
    completed_task = CompletedTasks.objects.get(id=task_ID)
    completed_task.delete()
    messages.success(request, 'Task removed successfully!')
    return redirect('show_tasks_completed')

# Concluir task
@csrf_exempt
@requires_csrf_token
@login_required()
def complete_task(request, task_ID):
    task = get_object_or_404(Task, id=task_ID)

    completed_task = CompletedTasks()

    completed_task.id = task.id
    completed_task.task = task.task
    completed_task.description = task.description
    completed_task.date_task = task.date_task
    completed_task.priority_level = task.priority_level
    completed_task.user_owner_task = task.user_owner_task

    completed_task.save()
    messages.success(request, 'Task completed successfully!')
    task.delete()

    return redirect('show_tasks_completed')


@csrf_exempt
@requires_csrf_token
@login_required()
def reverse_completion(request, task_ID):
    completed_task = get_object_or_404(CompletedTasks, id=task_ID)

    task = Task()

    task.id = completed_task.id
    task.task = completed_task.task
    task.description = completed_task.description
    task.date_task = completed_task.date_task
    task.priority_level = completed_task.priority_level
    task.user_owner_task = completed_task.user_owner_task

    task.save()
    messages.success(request, 'Successfully reversed task completion!')
    completed_task.delete()

    return redirect('show_tasks')

def delete_account(request):
    pass