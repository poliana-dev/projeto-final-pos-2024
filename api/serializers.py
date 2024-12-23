from rest_framework import serializers
from rest_framework import viewsets
from .models import *

class AcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acessorio
        fields = '__all__'

class CenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cenario
        fields = '__all__'

class PersonagemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Personagem
        fields = '__all__'  


class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Filme
        fields = '__all__'

    def getCenario(self, instance):
        cenario = super().getCenario(instance)
        filme_pk = self.context.get('filme_pk')

        if filme_pk is not None and instance.filme_id != int(filme_pk):
            return {}
        
        return cenario
    
    def getPersonagem(self, instance):
        personagem = super().getPersonagem(instance)
        filme_pk = self.context.get('filme_pk')

        if filme_pk is not None and instance.filme_id != int(filme_pk):
            return {}
        
        return personagem 
    
    def getAcessorio(self, instance):
        acessorio = super().getAcessorio(instance)  
        filme_pk = self.context.get('filme_pk')

        if filme_pk is not None and instance.filme_id != int(filme_pk):
            return {}
        return acessorio 
    

class MusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musica
        fields = '__all__'

    def getFilme(self, instance):
        filme = super().getFilme(instance)
        musica_pk = self.context.get('musica_pk')

        if musica_pk is not None and instance.musica_id != int(musica_pk):
            return {}
        return filme
    

class RoupaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Roupa
        fields = '__all__'

    def getPersonagem(self, instance):
        personagem = super().getPersonagem(instance)
        roupa_pk = self.context.get('roupa_pk')

        if roupa_pk is not None and instance.roupa_id != int(roupa_pk):
            return {}
        
        return personagem

    


