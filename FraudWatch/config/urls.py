from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),

    path('golpes/', GolpesView.as_view(), name='golpes'),

    path('links/', LinksView.as_view(), name='links'),

    path('mensagens/', MensagensView.as_view(), name='mensagens'),

    path('quiz/', QuizView.as_view(), name='quiz'),

    path('dicas/', DicasView.as_view(), name='dicas'),

    path('denuncias/', DenunciasView.as_view(), name='denuncias'),

    path('notificacoes/', NotificacoesView.as_view(), name='notificacoes'),
]