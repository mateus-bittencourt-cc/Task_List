from django.db import models

class Task(models.Model):
    content = models.CharField(max_length=255)
    concluida = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content