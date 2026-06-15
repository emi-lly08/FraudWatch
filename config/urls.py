from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),

    path('login/', LoginView.as_view(), name='login'),

    path('cadastro/', CadastroView.as_view(), name='cadastro'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('tipousuario/', TipoUsuarioView.as_view(), name='tipousuario'),

    path('usuario/', UsuarioView.as_view(), name='usuario'),

    path('categoriagolpe/', CategoriaGolpeView.as_view(), name='categoriagolpe'),

    path('golpedigital/', GolpeDigitalView.as_view(), name='golpedigital'),

    path('linksuspeito/', LinkSuspeitoView.as_view(), name='linksuspeito'),

    path('plataforma/', PlataformaView.as_view(), name='plataforma'),

    path(
        'mensagemfraudulenta/',
        MensagemFraudulentaView.as_view(),
        name='mensagemfraudulenta'
    ),

    path('quiz/', QuizView.as_view(), name='quiz'),

    path('pergunta/', PerguntaView.as_view(), name='pergunta'),

    path('resposta/', RespostaView.as_view(), name='resposta'),

    path(
        'dicaseguranca/',
        DicaSegurancaView.as_view(),
        name='dicaseguranca'
    ),

    path('denuncia/', DenunciaView.as_view(), name='denuncia'),

    path('notificacao/', NotificacaoView.as_view(), name='notificacao'),
]