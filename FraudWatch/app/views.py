from django.shortcuts import render
from django.views import View
from .models import *


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class TipoUsuarioView(View):
    def get(self, request, *args, **kwargs):
        tipousuarios = TipoUsuario.objects.all()
        return render(request, 'tipousuario.html', {'tipousuarios': tipousuarios})


class UsuarioView(View):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        return render(request, 'usuario.html', {'usuarios': usuarios})


class CategoriaGolpeView(View):
    def get(self, request, *args, **kwargs):
        categorias = CategoriaGolpe.objects.all()
        return render(request, 'categoriagolpe.html', {'categorias': categorias})


class GolpeDigitalView(View):
    def get(self, request, *args, **kwargs):
        golpes = GolpeDigital.objects.all()
        return render(request, 'golpedigital.html', {'golpes': golpes})


class LinkSuspeitoView(View):
    def get(self, request, *args, **kwargs):
        links = LinkSuspeito.objects.all()
        return render(request, 'linksuspeito.html', {'links': links})


class PlataformaView(View):
    def get(self, request, *args, **kwargs):
        plataformas = Plataforma.objects.all()
        return render(request, 'plataforma.html', {'plataformas': plataformas})


class MensagemFraudulentaView(View):
    def get(self, request, *args, **kwargs):
        mensagens = MensagemFraudulenta.objects.all()
        return render(request, 'mensagemfraudulenta.html', {'mensagens': mensagens})


class QuizView(View):
    def get(self, request, *args, **kwargs):
        quizzes = Quiz.objects.all()
        return render(request, 'quiz.html', {'quizzes': quizzes})


class PerguntaView(View):
    def get(self, request, *args, **kwargs):
        perguntas = Pergunta.objects.all()
        return render(request, 'pergunta.html', {'perguntas': perguntas})


class RespostaView(View):
    def get(self, request, *args, **kwargs):
        respostas = Resposta.objects.all()
        return render(request, 'resposta.html', {'respostas': respostas})


class DicaSegurancaView(View):
    def get(self, request, *args, **kwargs):
        dicas = DicaSeguranca.objects.all()
        return render(request, 'dicaseguranca.html', {'dicas': dicas})


class DenunciaView(View):
    def get(self, request, *args, **kwargs):
        denuncias = Denuncia.objects.all()
        return render(request, 'denuncia.html', {'denuncias': denuncias})


class NotificacaoView(View):
    def get(self, request, *args, **kwargs):
        notificacoes = Notificacao.objects.all()
        return render(request, 'notificacao.html', {'notificacoes': notificacoes})