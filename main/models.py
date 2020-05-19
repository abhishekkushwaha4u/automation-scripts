from django.db import models

class Script(models.Model):
    name = models.CharField(max_length=300)
    url = models.URLField()
    category = models.TextField(blank=True)
    added_on = models.DateTimeField(auto_now_add=True)
