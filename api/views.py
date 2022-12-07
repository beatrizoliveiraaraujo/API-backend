from django.shortcuts import render

from api.serializer import AdicionarImagensSerializer, CartaoSerializer, ClienteSerializer, ContaSerializer, EmprestimoSerializer, EnderecoSerializer, ExtratoSerializer, FaturaSerializer, ImagensSerializer, TranferenciaSerializer, UsuarioSerializer
from rest_framework import viewsets
from .models import Conta, Imagens,Usuario,Endereco,Cliente,Cartao,Tranferencia,Extrato,Emprestimo,Fatura

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

class CartaoViewSet(viewsets.ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer

class TranferenciaViewSet(viewsets.ModelViewSet):
    queryset = Tranferencia.objects.all()
    serializer_class = TranferenciaSerializer

class ExtratoViewSet(viewsets.ModelViewSet):
    queryset = Extrato.objects.all()
    serializer_class = ExtratoSerializer

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class FaturaViewSet(viewsets.ModelViewSet):
    queryset = Fatura.objects.all()
    serializer_class = FaturaSerializer

class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagens.objects.all()
    serializer_class = ImagensSerializer

class AdicionarImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagens.objects.all()
    serializer_class = AdicionarImagensSerializer




