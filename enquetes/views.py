from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Olá, Index!')


def detalhes(request, questao_id):
    return HttpResponse('Questão : %s.' % questao_id)


def resultados(request, questao_id):
    response = 'Questão: %s.'
    return HttpResponse(response % questao_id)


def votos(request, questao_id):
    return HttpResponse('Você votou na questão: %s.' % questao_id)
