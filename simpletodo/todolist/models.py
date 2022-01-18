from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)