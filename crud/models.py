from django.db import models

class user(models.Model):
    '''Model definition for user.'''

    nome = models.CharField(max_length=250,null=True)
    email = models.EmailField(max_length=250,null=False,unique=True)
    senha = models.CharField(max_length=256,null=False,unique=True)

    class Meta:
        '''Meta definition for user.'''
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        pass
