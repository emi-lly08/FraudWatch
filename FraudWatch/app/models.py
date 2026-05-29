from django.db import models


class TipoUsuario(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do tipo de usuário")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Usuário"
        verbose_name_plural = "Tipos de Usuários"


class Usuario(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do usuário")
    email = models.EmailField(verbose_name="Email do usuário")
    senha = models.CharField(max_length=50, verbose_name="Senha do usuário")
    idade = models.IntegerField(verbose_name="Idade do usuário")

    tipo_usuario = models.ForeignKey(
        TipoUsuario,
        on_delete=models.CASCADE,
        verbose_name="Tipo de usuário"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class CategoriaGolpe(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome da categoria")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria de Golpe"
        verbose_name_plural = "Categorias de Golpes"


class GolpeDigital(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título do golpe")
    descricao = models.TextField(verbose_name="Descrição do golpe")
    nivel_risco = models.CharField(max_length=50, verbose_name="Nível de risco")

    categoria = models.ForeignKey(
        CategoriaGolpe,
        on_delete=models.CASCADE,
        verbose_name="Categoria do golpe"
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Golpe Digital"
        verbose_name_plural = "Golpes Digitais"

class LinkSuspeito(models.Model):
    url = models.URLField(verbose_name="URL")
    descricao = models.TextField(verbose_name="Descrição")
    nivel_perigo = models.CharField(max_length=50, verbose_name="Nível de perigo")
    data_cadastro = models.DateTimeField(verbose_name="Data de cadastro")

    golpe = models.ForeignKey(
        GolpeDigital,
        on_delete=models.CASCADE,
        verbose_name="Golpe digital"
    )

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = "Link Suspeito"
        verbose_name_plural = "Links Suspeitos"


class Plataforma(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome da plataforma")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Plataforma"
        verbose_name_plural = "Plataformas"


class MensagemFraudulenta(models.Model):
    conteudo = models.TextField(verbose_name="Conteúdo")
    nivel_risco = models.CharField(max_length=50, verbose_name="Nível de risco")

    plataforma = models.ForeignKey(
        Plataforma,
        on_delete=models.CASCADE,
        verbose_name="Plataforma"
    )

    def __str__(self):
        return self.conteudo

    class Meta:
        verbose_name = "Mensagem Fraudulenta"
        verbose_name_plural = "Mensagens Fraudulentas"

class Quiz(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"


class Pergunta(models.Model):
    enunciado = models.TextField(verbose_name="Enunciado")
    alternativa_correta = models.CharField(max_length=100, verbose_name="Alternativa correta")

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        verbose_name="Quiz"
    )

    def __str__(self):
        return self.enunciado

    class Meta:
        verbose_name = "Pergunta"
        verbose_name_plural = "Perguntas"


class Resposta(models.Model):
    descricao = models.TextField(verbose_name="Descrição")
    correta = models.BooleanField(verbose_name="Correta")

    pergunta = models.ForeignKey(
        Pergunta,
        on_delete=models.CASCADE,
        verbose_name="Pergunta"
    )

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Resposta"
        verbose_name_plural = "Respostas"


class DicaSeguranca(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Dica de Segurança"
        verbose_name_plural = "Dicas de Segurança"


class Denuncia(models.Model):
    descricao = models.TextField(verbose_name="Descrição")
    data = models.DateTimeField(verbose_name="Data")
    status = models.CharField(max_length=50, verbose_name="Status")

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        verbose_name="Usuário"
    )

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Denúncia"
        verbose_name_plural = "Denúncias"


class Notificacao(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    mensagem = models.TextField(verbose_name="Mensagem")
    data = models.DateTimeField(verbose_name="Data")

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        verbose_name="Usuário"
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Notificação"
        verbose_name_plural = "Notificações"
