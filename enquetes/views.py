from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Questao


def index(request):
    lista_ultimas_questoes = Questao.objects.order_by('-data_pub')[:5]
    return render(request, 'enquetes/index.html', {'lista_ultimas_questoes': lista_ultimas_questoes})


def detalhes(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'enquetes/detalhes.html', {'questao': questao})


def resultados(request, questao_id):
    response = 'Resultado questão: %s.'
    return HttpResponse(response % questao_id)


def votos(request, questao_id):
    return HttpResponse('Você votou na questão: %s.' % questao_id)
