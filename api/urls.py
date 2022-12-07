from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_nested import routers

rota = routers.DefaultRouter()

rota.register('usuario/', views.UsuarioViewSet)
rota.register('endereco/', views.EnderecoViewSet)
rota.register('cliente/', views.ClienteViewSet)
rota.register('conta/', views.ContaViewSet)
rota.register('cartao/', views.CartaoViewSet)
rota.register('transferencia/', views.TranferenciaViewSet)
rota.register('extrato/', views.ExtratoViewSet)
rota.register('emprestimo/', views.EmprestimoViewSet)
rota.register('fatura/', views.FaturaViewSet)
rota.register('imagem/', views.ImagemViewSet)
rota.register('adicionar-imagem/', views.AdicionarImagemViewSet)


urlpatterns = rota.urls