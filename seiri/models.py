from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class Task(models.Model):

    PRIORITY = (
        ('High', 'High'),
        ('Normal', 'Normal'),
        ('Low', 'Low'),
    )

    id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    date_task = models.DateField(null=False, blank=False)
    priority_level = models.CharField(max_length=6, null=False, choices=PRIORITY)
    user_owner_task = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    



class CompletedTasks(models.Model):

    PRIORITY = (
        ('High', 'High'),
        ('Normal', 'Normal'),
        ('Low', 'Low'),
    )

    id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    date_task = models.DateField(null=False, blank=False)
    priority_level = models.CharField(max_length=6, null=False, choices=PRIORITY)
    user_owner_task = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.task
