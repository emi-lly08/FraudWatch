from django.contrib import admin
from .models import *

admin.site.register(TipoUsuario)
admin.site.register(Usuario)

admin.site.register(CategoriaGolpe)
admin.site.register(GolpeDigital)
admin.site.register(LinkSuspeito)

admin.site.register(Plataforma)
admin.site.register(MensagemFraudulenta)

admin.site.register(Quiz)
admin.site.register(Pergunta)
admin.site.register(Resposta)

admin.site.register(DicaSeguranca)

admin.site.register(Denuncia)
admin.site.register(Notificacao)