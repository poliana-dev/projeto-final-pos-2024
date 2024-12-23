from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import *
from .serializers import *

class AcessorioViewSet(viewsets.ModelViewSet):
    queryset= Acessorio.objects.all()
    serializer_class = AcessorioSerializer

class CenarioViewSet(viewsets.ModelViewSet):
    queryset = Cenario.objects.all()
    serializer_class = CenarioSerializer

class PersonagemViewSet(viewsets.ModelViewSet):
    serializer_class = PersonagemSerializer

    def get_queryset(self):
        personagem_pk = self.kwargs.get('personagem_pk')
        if personagem_pk:
            return Personagem.objects.filter(personagem_id = personagem_pk)
        return Personagem.objects.all()
    
class FilmeViewSet(viewsets.ModelViewSet):
    
    serializer_class = FilmeSerializer

    def get_queryset(self):
        filme_pk = self.kwargs.get('filme_pk')

        if filme_pk:
            return Filme.objects.filter(filme_id= filme_pk)
        return Filme.objects.all()

class MusicaViewSet(viewsets.ModelViewSet):
    serializer_class = MusicaSerializer

    def get_queryset(self):
        musica_pk = self.kwargs.get('musica_pk')

        if musica_pk:
            return Musica.objects.filter(musica_id = musica_pk)
        return Musica.objects.all() 
    

class RoupaViewSet(viewsets.ModelViewSet):
    serializer_class = RoupaSerializer

    def get_queryset(self):
        roupa_pk = self.kwargs.get('roupa_pk')

        if roupa_pk:
            return Roupa.objects.filter(musica_id = roupa_pk)
        return Roupa.objects.all() 
    


     
