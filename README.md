# Aplicação Seiri Task Manager

Projeto prático desenvolvido para a disciplina de engenharia web do curso Sistemas de Informação da Universidade Federal dos Vales do Jequitinhonha 
e Mucuri - UFVJM - Campus JK. O intuito era desenvolver uma aplicação que implementasse alguns dos conceitos da disciplina. O que foi um desafio! Muitos não foram implementados, 
principalmente devido a minha pouca experiência com o framework Django. O projeto estético da aplicação pode ser conferido neste [link](https://www.figma.com/file/pRKXLROwfJH8XkU3K8Hm7n/eng-web?node-id=1%3A4) e executado [aqui]().
Mas é definitivamente, o projeto que mais tenho orgulho de ter desenvolvido. Foi uma ótima experiência e sempre podemos dar uma incrementada, não é mesmo?! :sunglasses:        

![landing-page](https://user-images.githubusercontent.com/66737248/188193685-d6b3ee30-eae8-4a57-bd83-d219d50308d6.png)
![home](https://user-images.githubusercontent.com/66737248/189916688-53dea80c-579c-4805-9068-e20f190f9ed5.png)

### Status do Projeto

[![Status Completo](https://img.shields.io/badge/STATUS-COMPLETO-green?style=for-the-badge)]()

O projeto pode ser executado. Entretanto, há alguns requisitos que não foram ainda implementados.


### Funcionalidades da Aplicação
- [x] Login e Logout
- [x] Cadastro de usuários
- [x] Criação de tarefas
- [x] Listagem de tarefas a fazer ordenadas por data de forma ascendente.
- [x] Edição de tarefas (:warning: Apesar de persistir a data de forma correta no BD, a mesma não é retornada no modal de edição. :relieved:)
- [x] Remoção de tarefas
- [x] Conclusão de tarefas
- [x] Listagem de tarefas concluídas 
  
  
### Requisitos

* [ Django]( https://www.djangoproject.com/) - Framework Python 
* [ psycopg2](https://pypi.org/project/psycopg2/) -Banco de Dados
* [ pycharm]( https://www.jetbrains.com/pt-br/pycharm/download/) - IDE (Ambiente de Desenvolvimento)  
* Outros requisitos se encontram listados no arquivo ``requirements.txt`` neste repositório.

### Tecnologias

* HTML
* CSS
* Bootstrap 5
* Python - Framework Django
* PostgreSQL - Banco de Dados

### Processo de Execução da Aplicação

- *Passo 1* - Abra a pasta da aplicação no PyCharm.
- *Passo 2* - Instale os packages ``psycopg2`` e ``django`` via "python packages" na barra inferior da IDE.
- *Passo 3* - Crie um banco de dados PostgreSQL para a aplicação.
- *Passo 4* - Abra o arquivo ``settings.py`` e em ``DATABASES`` configure: 

```commandline
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', ''),
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASS', ''),
        'HOST': '',
        'PORT': '',
    }
}
```

- *Passo 5* - Abra o terminal do PyCharm e navegue até a pasta "projeto_seiri" (digite ``cd projeto_seiri``).
- *Passo 6* - Ainda no terminal, digite ```python manage.py runserver```.
- *Passo 7* - Copie o  endereço que será retornado ou clique ``CTRL + clique no endereço`` para abrir o navegador com a aplicação em execução!

```
System check identified no issues (0 silenced).
August 16, 2022 - 13:20:45
Django version 4.0.6, using settings 'projeto_seiri.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

- *Passo 8* - E prontim! Estará rodando a aplicação! 


## Autor

Aguinele Queiroz da Silva
