# Generated by Django 5.1.7 on 2025-04-05 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='func_registrar_produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=11)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='produtos/')),
                ('data_criacao', models.DateTimeField(auto_now=True, verbose_name='Data de criação')),
            ],
        ),
    ]
