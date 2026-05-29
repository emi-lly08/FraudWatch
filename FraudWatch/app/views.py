from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class GolpesView(View):
    def get(self, request, *args, **kwargs):
        golpes = GolpeDigital.objects.all()

        return render(
            request,
            'golpes.html',
            {'golpes': golpes}
        )


class LinksView(View):
    def get(self, request, *args, **kwargs):
        links = LinkSuspeito.objects.all()

        return render(
            request,
            'links.html',
            {'links': links}
        )


class MensagensView(View):
    def get(self, request, *args, **kwargs):
        mensagens = MensagemFraudulenta.objects.all()

        return render(
            request,
            'mensagens.html',
            {'mensagens': mensagens}
        )


class QuizView(View):
    def get(self, request, *args, **kwargs):
        quizzes = Quiz.objects.all()

        return render(
            request,
            'quiz.html',
            {'quizzes': quizzes}
        )


class DicasView(View):
    def get(self, request, *args, **kwargs):
        dicas = DicaSeguranca.objects.all()

        return render(
            request,
            'dicas.html',
            {'dicas': dicas}
        )


class DenunciasView(View):
    def get(self, request, *args, **kwargs):
        denuncias = Denuncia.objects.all()

        return render(
            request,
            'denuncias.html',
            {'denuncias': denuncias}
        )


class NotificacoesView(View):
    def get(self, request, *args, **kwargs):
        notificacoes = Notificacao.objects.all()

        return render(
            request,
            'notificacoes.html',
            {'notificacoes': notificacoes}
        )