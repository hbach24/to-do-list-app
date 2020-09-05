from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    made = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title