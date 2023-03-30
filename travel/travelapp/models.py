from django.db import models


# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    img = models.FileField(upload_to='pics/')
    desc = models.TextField()


class team(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    img = models.FileField(upload_to='pics/')
    desc = models.TextField()


def __str__(self):
    return self.place.name
    return self.team.name
