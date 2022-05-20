from datetime import datetime
from sqlite3 import Date
from xmlrpc.client import _datetime
from django.db import models
from django.forms import DateField

# Create your models here.

class Funcionario (models.Model):
    Nome = models.CharField(max_length=50)
    Salario = models.DecimalField(decimal_places=2, max_digits=8)
    Data_admissao = models.DateField(Date)
    Data_demissao = models.DateField(Date)
    Feedback_pos = models.IntegerField(max_length=2)
    Feedback_neg = models.IntegerField(max_length=2)
    Avaliacao = models.IntegerField(max_length=2)

class Cargo (models.Model):
    Nome = models.CharField(max_length=150)
    Sal_min = models.DecimalField(decimal_places=2,max_digits=8)
    Sal_max = models.DecimalField(decimal_places=2,max_digits=8)

class Departamento (models.Model):
	ID_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
	ID_funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
	Departamento = models.CharField(max_length=150)

class Fiscal (models.Model):
    Num_nota = models.IntegerField(max_length=20)
    Valor = models.DecimalField(decimal_places=2,max_digits=15)
    Itens = models.CharField(max_length=150)

class Financeiro(models.Model):
	ID_Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
	ID_Fiscal = models.ForeignKey(Fiscal, on_delete=models.CASCADE)
	Receita_despesa = models.BooleanField(max_length=1)
	Valor = models.DecimalField(decimal_places=2,max_digits=2)