from django.shortcuts import render, get_object_or_404, redirect
from App.models import Tarefa, TarefasConcluidas
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from App.form_usuario import FormLogin, FormCadastro
from django.contrib import messages


User = get_user_model()


# Cadastrar usuário
def cadastrar(request):
    formulario_usuario = FormCadastro(request.POST or None)
    if formulario_usuario.is_valid():
        username = formulario_usuario.cleaned_data.get("username")
        email = formulario_usuario.cleaned_data.get("email")
        password = formulario_usuario.cleaned_data.get("password1")
        password2 = formulario_usuario.cleaned_data.get("password2")
        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None
        if user != None:
            login(request, user)
            messages.success(request, f'Bem vindo, {user.get_username()}!')
            return HttpResponseRedirect("listagem_tarefas")
        else:
            request.session['register_error'] = 1 # 1 == True
    return render(request, "register-page.html", {"formulario_usuario": formulario_usuario})


#login de usuário
def entrar(request):
    formulario_login = FormLogin(request.POST or None)
    
    if formulario_login.is_valid():

        username = formulario_login.cleaned_data.get("username")
        password = formulario_login.cleaned_data.get("password")
        usuario = authenticate(request, username=username, password=password)

        if usuario != None:
            login(request, usuario)
            messages.success(request, f'Bem vindo, {usuario.get_username()}!')
            return HttpResponseRedirect("listagem_tarefas")
        else:
            messages.error(request, 'Usuário ou senha inválido!')
            request.session['invalid_user'] = 1 # 1 == True
    return render(request, "login-page.html", {"formulario_login": formulario_login})

# logout
@login_required()
def sair(request):
    logout(request)
    return HttpResponseRedirect("entrar")

# informações de perfil
def perfil_usuario(request):
    if request.method == 'GET':
        return render(request, 'modal-informacoes-perfil.html')

# alterar senha de usuario
def alterar_senha(request):
    pass

# homepage
def home(request):
    return render(request, 'promocional-page.html')

# pagina_principal
@login_required()
def listagem_tarefas(request):
    lista_tarefas = Tarefa.objects.all().filter(usuario = request.user).order_by('data')
    return render(request, 'lista-tarefas.html', {"tarefas": lista_tarefas})

# pagina_principal
@login_required()
def listagem_tarefas_concluidas(request):
    lista_tarefas_concluidas = TarefasConcluidas.objects.all().filter(usuario = request.user).order_by('data')
    return render(request, 'tarefas-concluidas.html', {"tarefas_concluidas": lista_tarefas_concluidas})

# Adicionar tarefa
@login_required()
def adicionar_tarefa(request):
    if request.method == "POST":
        if request.POST.get('tarefa') \
            and request.POST.get('descricao') \
            and request.POST.get('data') \
            or request.POST.get('prioridade'):
            tarefa = Tarefa()
            tarefa.tarefa = request.POST.get('tarefa')
            tarefa.descricao = request.POST.get('descricao')
            tarefa.data = request.POST.get('data')
            tarefa.prioridade = request.POST.get('prioridade')
            tarefa.usuario = request.user
            tarefa.save()

            messages.success(request, 'Tarefa Adicionada com sucesso!')

            return HttpResponseRedirect('listagem_tarefas')
    else:
        return render(request, 'modal-adicionar-tarefa.html')

# Visualizar tarefa individualmente
@login_required()
def tarefa(request, tarefa_id):
    tarefa = Tarefa.objects.get(
        id = tarefa_id
    )
    if tarefa != None:
        return render(request, "modal-editar-tarefa.html", {'tarefa': tarefa})


# Editar tarefa
@login_required()
def editar_tarefa(request):
    if request.method == "POST":
        tarefa = Tarefa.objects.get(id = request.POST.get('id'))
        if tarefa != None:
            tarefa.tarefa = request.POST.get('tarefa')
            tarefa.descricao = request.POST.get('descricao')
            tarefa.data = request.POST.get('data')
            tarefa.prioridade = request.POST.get('prioridade')
            tarefa.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return HttpResponseRedirect('listagem_tarefas')


# Remover tarefa
@login_required()
def remover_tarefa(request, tarefa_id):
    tarefa = Tarefa.objects.get( id = tarefa_id )
    tarefa.delete()
    messages.success(request, 'Tarefa removida com sucesso!')
    return redirect('listagem_tarefas')

# Remover tarefa
@login_required()
def remover_tarefa_concluida(request, tarefa_id):
    tarefa_concluida = TarefasConcluidas.objects.get( id = tarefa_id )
    tarefa_concluida.delete()
    messages.success(request, 'Tarefa removida com sucesso!')
    return redirect('listagem_tarefas_concluidas')

# Concluir tarefa
@login_required()
def concluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404( Tarefa, id = tarefa_id )

    tarefa_concluida = TarefasConcluidas()

    tarefa_concluida.id = tarefa.id
    tarefa_concluida.tarefa = tarefa.tarefa
    tarefa_concluida.descricao = tarefa.descricao
    tarefa_concluida.data = tarefa.data
    tarefa_concluida.prioridade = tarefa.prioridade
    tarefa_concluida.usuario = tarefa.usuario

    tarefa_concluida.save()
    messages.success(request, 'Tarefa Concluída com sucesso!')
    tarefa.delete()

    return redirect('listagem_tarefas_concluidas')

# Desfazer conclusão
@login_required()
def desfazer_conclusao(request, tarefa_id):
    tarefa_concluida = get_object_or_404( TarefasConcluidas, id = tarefa_id )

    tarefa = Tarefa()

    tarefa.id = tarefa_concluida.id
    tarefa.tarefa = tarefa_concluida.tarefa
    tarefa.descricao = tarefa_concluida.descricao
    tarefa.data = tarefa_concluida.data
    tarefa.prioridade = tarefa_concluida.prioridade
    tarefa.usuario = tarefa_concluida.usuario

    tarefa.save()
    messages.success(request, 'Conclusão de tarefa cancela com sucesso!')
    tarefa_concluida.delete()

    return redirect('listagem_tarefas')

# mostrar calendario
# @login_required()
# def mostrar_calendario(request):
#     return render(request, 'modal-calendario.html')