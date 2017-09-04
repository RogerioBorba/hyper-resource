from __future__ import unicode_literals
from hyper_resource.models import FeatureModel, BusinessModel

from hyper_resource.models import  BusinessModel
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Usuario(BusinessModel):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True)
    email = models.CharField(null=True, max_length=100)
    senha = models.CharField(max_length=50)

class TipoGasto(BusinessModel):
    nome = models.CharField(max_length=100)

class Gasto(BusinessModel):
    data = models.DateField(null=True)
    tipo_gasto = models.ForeignKey(TipoGasto)
    usuario = models.ForeignKey(Usuario, related_name='gastos')
    valor = models.FloatField()

