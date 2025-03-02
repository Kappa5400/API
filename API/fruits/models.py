from django.db import models

class fruit(models.Model):
    name = models.CharField(max_length=200)
    rank = models.IntegerField(max_length=100)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.name


