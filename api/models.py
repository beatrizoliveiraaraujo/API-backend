from msilib.schema import Class
from turtle import mode
from wsgiref.validate import validator
from xmlrpc.client import boolean
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from pictures.models import PictureField

from banco.settings import PICTURES

class Usuario(models.Model):

    cpf = models.CharField(max_length=11)
    senha = models.CharField(max_length=11)

class tipos_clientes(models.Model):

    Platinum = 'P'
    Gold = 'B'

    CLIENTES_TIPOS = [
        (Platinum, 'Platinum'),
        (Gold, 'Basico')
    ]
    tipo = models.CharField(max_length=1, choices=CLIENTES_TIPOS, default= Gold)

class Endereco(models.Model):

    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    
class Cliente(models.Model):

    nome = models.CharField(max_length=225, null=True)
    email = models.EmailField(max_length=50, unique=True)
    celular = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    


class Conta(models.Model):
    agencia = models.CharField(max_length=4)
    conta = models.CharField(max_length=9)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=20, decimal_places=2)

class Cartao(models.Model):
    senha = models.CharField(max_length=11)
    agencia = models.CharField(max_length=4)
    conta = models.CharField(max_length=9)
    validade = models.DateField()
    codigo_seguranca = models.CharField(max_length=3)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    bandeira = models.CharField(max_length=11)

class Tranferencia(models.Model):
    remetente = models.ForeignKey(Conta, on_delete=models.CASCADE,related_name='remetente')
    destinatario = models.ForeignKey(Conta, on_delete=models.CASCADE,related_name='destinatario')
    valor = models.DecimalField(max_digits=10,decimal_places=2)

class Extrato(models.Model):
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    tranferencia = models.ForeignKey(Tranferencia, on_delete=models.CASCADE)

class Emprestimo(models.Model):
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    parcela = models.IntegerField()
    aprovacao = models.BooleanField()
    qtdparcelas = models.IntegerField()
    valor_com_juros = models.IntegerField()
    data_Primeira_Parcela = models.DateTimeField()
    situacao = models.CharField(max_length=11)

class Fatura(models.Model):
    cartao = models.ForeignKey(Cartao, on_delete=models.CASCADE)
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)
    

class Imagens(models.Model):
    titulo = models.CharField(max_length=255)
    foto = PictureField(upload_to='api/imagens')


