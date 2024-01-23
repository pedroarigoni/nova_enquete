import datetime
from django.db import models
from django.utils import timezone


class Questao(models.Model):
    titulo_questao = models.CharField(max_length=200)
    data_pub = models.DateTimeField('date published')

    def __str__(self):
        return self.titulo_questao

    def foi_publicado_recentemente(self):
        return self.data_pub >= timezone.now() - datetime.timedelta(days=1)


class Opcao(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    titulo_opcao = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo_opcao
