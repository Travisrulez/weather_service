from django.db import models

class User(models.Model):
    nickname = models.CharField(verbose_name='50' , max_length=50)
    password = models.CharField(verbose_name='50', max_length=50)

    class Meta: 
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.nickname
