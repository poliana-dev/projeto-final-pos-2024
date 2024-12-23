from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_nested.routers import NestedDefaultRouter 


from api import views

router = routers.DefaultRouter()

###### rotas brutas #####

router.register(r'personagens', views.PersonagemViewSet, basename='personagens')
router.register(r'acessorios', views.AcessorioViewSet, basename='acessorios')
router.register(r'filmes', views.FilmeViewSet, basename='filmes')
router.register(r'cenarios', views.CenarioViewSet, basename='cenarios')
router.register(r'musicas', views.MusicaViewSet, basename='musicas')
router.register(r'roupas', views.RoupaViewSet, basename='roupas')

#############################

###### rotas relacionadas ######

# aninhadas para filmes

filme_router =NestedDefaultRouter(router, r'filmes', lookup='filme')
filme_router.register(r'cenarios', views.CenarioViewSet, basename='filme-cenario')
filme_router.register(r'personagens', views.PersonagemViewSet, basename='filme-personagem')
filme_router.register(r'acessorios', views.AcessorioViewSet, basename='filme-acessorio')
filme_router.register(r'musicas', views.MusicaViewSet, basename='filme-musica')

# aninhada para personagens

personagem_router = NestedDefaultRouter(router, r'personagens', lookup='personagem')
personagem_router.register(r'roupas', views.RoupaViewSet, basename='personagem-roupa')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(filme_router.urls)),
    path('', include(personagem_router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)