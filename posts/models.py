from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=50)
    header = models.CharField(max_length=100)
    text = models.TextField()



    def __str__(self):
        return f"{self.header} by {self.name[:50]}"