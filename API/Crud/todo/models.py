from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length = 200)
    created = models.TimeField(auto_now_add=True)