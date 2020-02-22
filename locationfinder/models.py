from django.db import models


class reg(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    location = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


# Create your models here.
class add(models.Model):
    userid = models.CharField(max_length=100)
    locname = models.CharField(max_length=100)
    map = models.CharField(max_length=100)
    cover_img = models.ImageField(null=True)
    img_1 = models.ImageField(null=True)
    img_2 = models.ImageField(null=True)
    img_3 = models.ImageField(null=True)
    indro = models.TextField()
    desc = models.TextField()
    status = models.IntegerField()


class fed(models.Model):
    date = models.DateField()
    userid = models.CharField(max_length=100)
    feed = models.TextField(null=True)

class fedre(models.Model):
    date = models.DateField()
    userid = models.CharField(max_length=100)
    feedreplay = models.TextField(null=True)

class locre(models.Model):
    date = models.DateField()
    userid = models.CharField(max_length=100)
    locstatus = models.TextField(null=True)
