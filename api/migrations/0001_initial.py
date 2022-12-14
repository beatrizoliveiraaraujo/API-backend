# Generated by Django 4.1.2 on 2022-11-29 13:50

from django.db import migrations, models
import django.db.models.deletion
import pictures.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senha', models.CharField(max_length=11)),
                ('agencia', models.CharField(max_length=4)),
                ('conta', models.CharField(max_length=9)),
                ('validade', models.DateField()),
                ('codigo_seguranca', models.CharField(max_length=3)),
                ('bandeira', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=225, null=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('celular', models.CharField(max_length=10)),
                ('cpf', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agencia', models.CharField(max_length=4)),
                ('conta', models.CharField(max_length=9)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('parcela', models.IntegerField()),
                ('aprovacao', models.BooleanField()),
                ('qtdparcelas', models.IntegerField()),
                ('valor_com_juros', models.IntegerField()),
                ('data_Primeira_Parcela', models.DateTimeField()),
                ('situacao', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('foto', pictures.models.PictureField(aspect_ratios=[None], breakpoints={'l': 1200, 'm': 992, 's': 768, 'xl': 1400, 'xs': 576}, container_width=1200, file_types=['WEBP'], grid_columns=12, pixel_densities=[1, 2], upload_to='api/imagens')),
            ],
        ),
        migrations.CreateModel(
            name='tipos_clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('P', 'Platinum'), ('B', 'Basico')], default='B', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('senha', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Tranferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinatario', to='api.conta')),
                ('remetente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remetente', to='api.conta')),
            ],
        ),
        migrations.CreateModel(
            name='Fatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cartao')),
                ('emprestimo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.emprestimo')),
            ],
        ),
        migrations.CreateModel(
            name='Extrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.conta')),
                ('tranferencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tranferencia')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.endereco'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario'),
        ),
        migrations.AddField(
            model_name='cartao',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cliente'),
        ),
    ]
