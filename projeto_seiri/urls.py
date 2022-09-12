from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # homepage aplicacao
    path('', views.home, name="home"),

    #logar usuario
    path('entrar', views.entrar, name="entrar"),

    #informações de usuário
    path('perfil_usuario', views.perfil_usuario, name="perfil_usuario"),
    
    #informações de usuário
    path('alterar_senha', views.alterar_senha, name="alterar_senha"),

    #logar usuario
    path('sair', views.sair, name="sair"),

    #cadastrar usuario
    path('cadastrar', views.cadastrar, name="cadastrar"),

    # pagina_principal
    path('listagem_tarefas', views.listagem_tarefas, name="listagem_tarefas"),

    # pagina_principal
    path('listagem_tarefas_concluidas', views.listagem_tarefas_concluidas, name="listagem_tarefas_concluidas"),

    # Adicionar tarefa
    path('adicionar_tarefa', views.adicionar_tarefa, name="adicionar_tarefa"),

    # Editar tarefa
    path('editar_tarefa', views.editar_tarefa, name="editar_tarefa"),

    # Remover tarefa
    path('remover_tarefa/<str:tarefa_id>', views.remover_tarefa, name="remover_tarefa"),

    # Remover tarefa
    path('remover_tarefa_concluida/<str:tarefa_id>', views.remover_tarefa_concluida, name="remover_tarefa_concluida"),

    # Concluir tarefa
    path('concluir_tarefa/<str:tarefa_id>', views.concluir_tarefa, name="concluir_tarefa"),

    # Desfazer a conclusão de uma tarefa
    path('desfazer_conclusao/<str:tarefa_id>', views.desfazer_conclusao, name="desfazer_conclusao"),

    # Visualizar tarefa individualmente
    path('tarefa/<str:tarefa_id>', views.tarefa, name="tarefa")

    # # visualizar calendario
    # path('mostrar_calendario', views.mostrar_calendario, name="mostrar_calendario")
]

