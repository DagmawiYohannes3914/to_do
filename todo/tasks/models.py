from django.db import models

# Create your models here.


class TodoItem(models.Model):
    task = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task
