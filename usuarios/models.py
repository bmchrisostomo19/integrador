<<<<<<< HEAD
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=64)

    def __str__(self) -> str:
=======
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=64)

    def __str__(self) -> str:
>>>>>>> 1651482b46c304b36ab1d5056382003c08636891
        return self.nome