from dataclasses import fields
from decimal import Decimal
from rest_framework import serializers
from pictures.contrib.rest_framework import PictureField
from api.models import Usuario, Endereco, Cliente, Conta, Cartao,Tranferencia,Extrato,Emprestimo, Fatura, Imagens

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'cpf','senha']

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'estado', 'cidade', 'cep', 'bairro', 'numero']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'email', 'celular', 'cpf', 'usuario','endereco']

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['id', 'agencia', 'conta', 'cliente', 'saldo']
        
class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao
        fields = ['id', 'senha', 'agencia', 'conta', 'validade','codigo_seguranca', 'cliente','bandeira']  

class TranferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tranferencia
        fields = ['id', 'remetente', 'destinatario', 'valor']

class ExtratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extrato
        fields = ['id', 'conta', 'tranferencia']

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = ['id', 'valor', 'parcela', 'aprovacao', 'qtdparcelas','valor_com_juros', 'data_Primeira_Parcela','situacao']  

class FaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fatura
        fields = ['id', 'cartao', 'emprestimo']

class ImagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagens
        fields = ['id', 'titulo', 'foto']
    foto = PictureField()

class AdicionarImagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagens
        fields = ['id', 'titulo', 'foto']