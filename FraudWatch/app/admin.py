from django.contrib import admin
from .models import *


class GolpeDigitalInline(admin.TabularInline):
    model = GolpeDigital
    extra = 1


class PerguntaInline(admin.TabularInline):
    model = Pergunta
    extra = 1


class RespostaInline(admin.TabularInline):
    model = Resposta
    extra = 1


class MensagemFraudulentaInline(admin.TabularInline):
    model = MensagemFraudulenta
    extra = 1


@admin.register(CategoriaGolpe)
class CategoriaGolpeAdmin(admin.ModelAdmin):
    inlines = [GolpeDigitalInline]


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    inlines = [PerguntaInline]


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    inlines = [RespostaInline]


@admin.register(Plataforma)
class PlataformaAdmin(admin.ModelAdmin):
    inlines = [MensagemFraudulentaInline]


admin.site.register(TipoUsuario)
admin.site.register(Usuario)

admin.site.register(GolpeDigital)
admin.site.register(LinkSuspeito)

admin.site.register(MensagemFraudulenta)

admin.site.register(Resposta)

admin.site.register(DicaSeguranca)

admin.site.register(Denuncia)
admin.site.register(Notificacao)