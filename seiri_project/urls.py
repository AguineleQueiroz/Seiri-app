from django.contrib import admin
from django.urls import path, include

from seiri import views

urlpatterns = [
    path('accounts/', include('accounts.urls')),

    path('accounts/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),

    path('', views.home, name="home"),

    path('usr_profile', views.usr_profile, name="usr_profile"),

    path('show_tasks', views.show_tasks, name="show_tasks"),

    path('show_tasks_completed', views.show_tasks_completed, name="show_tasks_completed"),

    path('add', views.add, name="add"),

    path('update_task', views.update_task, name="update_task"),

    path('delete_task/<str:task_ID>', views.delete_task, name="delete_task"),
    
    path('delete_task_completed/<str:task_ID>', views.delete_task_completed, name="delete_task_completed"),

    path('complete_task/<str:task_ID>', views.complete_task, name="complete_task"),

    path('reverse_completion/<str:task_ID>', views.reverse_completion, name="reverse_completion"),

    path('task/<str:task_ID>', views.task, name="task"),

    path('completed_task/<str:task_ID>', views.completed_task, name="completed_task"),

    path('delete_account', views.delete_account, name="delete_account"),

]
