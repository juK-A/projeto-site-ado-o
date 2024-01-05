from django.db import models

# Create your models here.
class Adotante(models.Model): # Models para o banco de dados 
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    endereco = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.nome

class Dog(models.Model):  # Models para o banco de dados 
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    raca = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    MACHO = 'Macho'
    FEMEA = 'Femea'
    STATUS_CHOICES = [
        (MACHO, 'Macho'),
        (FEMEA, 'Femea'),
    ]
    sexo = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.nome
    