from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    pub_date = models.DateTimeField()

