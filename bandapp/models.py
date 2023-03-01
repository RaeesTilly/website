# created the bandapp models 
from django.db import models

# Create your models here.
class band(models.Model):
    """created 
    model for band app
    """
    title = models.CharField(max_length=500)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
