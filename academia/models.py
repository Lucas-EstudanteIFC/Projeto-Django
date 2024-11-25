from django.db import models

class Formacao(models.Model):
        nome = models.CharField(max_length=100)
        descricao = models.TextField(max_length=500)
        def __str__(self):
            return self.nome
    
class Instituicao(models.Model):
        nome = models.CharField(max_length=100)
        descricao = models.TextField(max_length=500)
        cidade = models.CharField(max_length=100)
        def __str__(self):
             return self.nome

class Instrutor(models.Model):
        nome = models.CharField(max_length=100)
        email = models.EmailField()
        data_nascimento = models.DateField(blank=True, null=True)
        def __str__(self):
              return self.nome