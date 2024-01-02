from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField ()
    status = models.CharField(max_length=20, default='Not Started')

    def __str__(self):
        return self.title
