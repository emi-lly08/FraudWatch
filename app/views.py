from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.utils import timezone

def usuario_logado(request):

    if not request.session.get('usuario_id'):
        return False

    return True

class IndexView(View):

    def get(self, request, *args, **kwargs):

        usuario_nome = request.session.get('usuario_nome')
        tipo_usuario = request.session.get('tipo_usuario')

        return render(
            request,
            'index.html',
            {
                'usuario_nome': usuario_nome,
                'tipo_usuario': tipo_usuario
            }
        )

class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):

        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            usuario = Usuario.objects.get(
                email=email,
                senha=senha
            )

            request.session['usuario_id'] = usuario.id
            request.session['usuario_nome'] = usuario.nome
            request.session['tipo_usuario'] = usuario.tipo_usuario.nome

            return redirect('/')

        except Usuario.DoesNotExist:

            return render(
                request,
                'login.html',
                {
                    'erro': 'Email ou senha inválidos.'
                }
            )

class CadastroView(View):

    def get(self, request):
        return render(request, 'cadastro.html')

    def post(self, request):

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        idade = request.POST.get('idade')

        tipo_usuario = TipoUsuario.objects.get(nome='Jovem')

        Usuario.objects.create(
            nome=nome,
            email=email,
            senha=senha,
            idade=idade,
            tipo_usuario=tipo_usuario
        )

        return redirect('/login/')
    
class LogoutView(View):

    def get(self, request):

        request.session.flush()

        return redirect('/login/')
    
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

        if not usuario_logado(request):
            return redirect('/login/')

        categorias = CategoriaGolpe.objects.all()

        return render(
            request,
            'categoriagolpe.html',
            {'categorias': categorias}
        )


class PlataformaView(View):

    def get(self, request, *args, **kwargs):

        if not usuario_logado(request):
            return redirect('/login/')

        plataformas = Plataforma.objects.all()

        return render(
            request,
            'plataforma.html',
            {'plataformas': plataformas}
        )
    
class GolpeDigitalView(View):

    def get(self, request, *args, **kwargs):

        if not usuario_logado(request):
            return redirect('/login/')

        golpes = GolpeDigital.objects.all()

        return render(
            request,
            'golpedigital.html',
            {'golpes': golpes}
        )


class LinkSuspeitoView(View):

    def get(self, request, *args, **kwargs):

        if not usuario_logado(request):
            return redirect('/login/')

        links = LinkSuspeito.objects.all()

        return render(
            request,
            'linksuspeito.html',
            {'links': links}
        )


class MensagemFraudulentaView(View):

    def get(self, request, *args, **kwargs):

        if not usuario_logado(request):
            return redirect('/login/')

        mensagens = MensagemFraudulenta.objects.all()

        return render(
            request,
            'mensagemfraudulenta.html',
            {'mensagens': mensagens}
        )


class QuizView(View):

    def get(self, request, *args, **kwargs):

        if not usuario_logado(request):
            return redirect('/login/')

        quizzes = Quiz.objects.all()

        return render(
            request,
            'quiz.html',
            {'quizzes': quizzes}
        )


class PerguntaView(View):

    def get(self, request, *args, **kwargs):

        if not usuario_logado(request):
            return redirect('/login/')

        perguntas = Pergunta.objects.all()

        return render(
            request,
            'pergunta.html',
            {'perguntas': perguntas}
        )


class RespostaView(View):

    def get(self, request, *args, **kwargs):

        if not usuario_logado(request):
            return redirect('/login/')

        respostas = Resposta.objects.all()

        return render(
            request,
            'resposta.html',
            {'respostas': respostas}
        )


class DicaSegurancaView(View):

    def get(self, request, *args, **kwargs):

        if not usuario_logado(request):
            return redirect('/login/')

        dicas = DicaSeguranca.objects.all()

        return render(
            request,
            'dicaseguranca.html',
            {'dicas': dicas}
        )


class DenunciaView(View):

    def get(self, request, *args, **kwargs):

        if not usuario_logado(request):
            return redirect('/login/')

        denuncias = Denuncia.objects.all()

        return render(
            request,
            'denuncia.html',
            {'denuncias': denuncias}
        )

    def post(self, request, *args, **kwargs):

        if not usuario_logado(request):
            return redirect('/login/')

        descricao = request.POST.get('descricao')

        usuario = Usuario.objects.get(
            id=request.session['usuario_id']
        )

        Denuncia.objects.create(
            descricao=descricao,
            data=timezone.now(),
            status='Pendente',
            usuario=usuario
        )

        return redirect('/denuncia/')

    def get(self, request, *args, **kwargs):

        if not usuario_logado(request):
            return redirect('/login/')

        denuncias = Denuncia.objects.all()

        return render(
            request,
            'denuncia.html',
            {'denuncias': denuncias}
        )


class NotificacaoView(View):

    def get(self, request, *args, **kwargs):

        if not usuario_logado(request):
            return redirect('/login/')

        notificacoes = Notificacao.objects.all()

        return render(
            request,
            'notificacao.html',
            {'notificacoes': notificacoes}
        )