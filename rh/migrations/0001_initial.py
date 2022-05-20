# Generated by Django 4.0.4 on 2022-05-20 20:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=150)),
                ('Sal_min', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Sal_max', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Departamento', models.CharField(max_length=150)),
                ('ID_cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rh.cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Fiscal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num_nota', models.IntegerField(max_length=20)),
                ('Valor', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Itens', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=50)),
                ('Salario', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Data_admissao', models.DateField(verbose_name=datetime.date)),
                ('Data_demissao', models.DateField(verbose_name=datetime.date)),
                ('Feedback_pos', models.IntegerField(max_length=2)),
                ('Feedback_neg', models.IntegerField(max_length=2)),
                ('Avaliacao', models.IntegerField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Financeiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Receita_despesa', models.BooleanField(max_length=1)),
                ('Valor', models.DecimalField(decimal_places=2, max_digits=2)),
                ('ID_Departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rh.departamento')),
                ('ID_Fiscal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rh.fiscal')),
            ],
        ),
        migrations.AddField(
            model_name='departamento',
            name='ID_funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rh.funcionario'),
        ),
    ]
