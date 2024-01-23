from django.db import models


class Questao(models.Model):
    titulo_questao = models.CharField(max_length=200)
    data_pub = models.DateTimeField('date published')


class Opcao(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    titulo_opcao = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
