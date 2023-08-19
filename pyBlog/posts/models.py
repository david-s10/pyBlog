import uuid

from django.db import models

from users.models import CustomUser


# Create your models here.


class Tags(models.Model):
    def __str__(self):
        return self

    name = models.CharField(max_length=100)


class Post(models.Model):
    def __str__(self):
        return self.title

    POST_STATUS = (('pb', 'published'), ('dr', 'draft'))

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=100, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to='static/images', null=True, blank=True)
    tags = models.ManyToManyField(Tags, blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data_pub = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=POST_STATUS, default='dr')


