from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=35, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    data_joined = models.DateField()

    create_at = models.DateTimeField(auto_now_add=True)