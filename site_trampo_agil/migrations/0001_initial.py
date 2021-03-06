# Generated by Django 2.1.7 on 2019-03-10 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidatos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('carreira', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=20)),
                ('confirmar_senha', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('nome_representante', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('carreira', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=20)),
                ('confirmar_senha', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vagas',
            fields=[
                ('cod', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('desc', models.TextField(max_length=1000)),
                ('salario', models.CharField(max_length=200)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_trampo_agil.Empresa')),
            ],
        ),
    ]
