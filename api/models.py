from django.db import models

class Acessorio(models.Model):
    nome= models.CharField(max_length=100, verbose_name="Nome do Acessório")
    descricao = models.TextField( verbose_name="Descrição")
    foto = models.ImageField(upload_to='acessorios', blank=True, null=True, verbose_name="Foto do acessório")

    def __str__(self):
        return f"{self.nome}"

class Personagem(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do personagem')
    foto = models.ImageField(upload_to='personagens', blank=True, null=True, verbose_name="Foto do personagem")
    descricao = models.TextField( verbose_name="Descrição")
    
    def __str__(self):
        return f"{self.nome}"


class Cenario(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do cenário")
    foto = models.ImageField(upload_to='cenarios', verbose_name="Foto do cenário")

    def __str__(self):
        return f"{self.nome}"

class Filme(models.Model):
    nome = models.CharField(max_length=100, verbose_name= "Nome do filme")
    duracao = models.CharField(max_length=80, verbose_name="Duração")
    ano = models.IntegerField(verbose_name="Ano de lançamento")
    capa = models.ImageField(upload_to='capa_filmes', verbose_name="Capa do filme")
    cenarios = models.ManyToManyField(Cenario, related_name='filmes')
    personagens = models.ManyToManyField(Personagem,related_name='filmes')
    acessorio = models.ManyToManyField(Acessorio, related_name='filmes', blank=True)


    def __str__(self):
        return f"{self.nome} ({self.ano})"
    

class Musica(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da música")
    duracao = models.CharField(max_length=45, verbose_name="Duração da música", help_text="Nesse formato: 3m30")
    url = models.URLField(verbose_name="Link da música", null=True)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, verbose_name="Filme", related_name='musicas')

    def __str__(self):
        return f"{self.nome} ({self.duracao})"
    
class Roupa(models.Model):
    descricao = models.TextField(verbose_name="Descrição")
    foto = models.ImageField(upload_to="roupas", verbose_name="Foto da vestimenta")
    personagem = models.ForeignKey(Personagem, on_delete=models.CASCADE, verbose_name="Personagem")

    def __str__(self):
        return f"{self.descricao}"
    


