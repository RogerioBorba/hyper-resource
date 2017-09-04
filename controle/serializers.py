from controle.models import *
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField

class GastoSerializer(ModelSerializer):
    tipo_gasto = HyperlinkedRelatedField(view_name='tipo_gasto_detail', many=False, read_only=True)
    usuario = HyperlinkedRelatedField(view_name='usuario_detail', many=False, read_only=True)
    class Meta:
        model = Gasto
        fields = ['id','data','tipo_gasto','usuario','valor']
        identifier = 'id'
        identifiers = '[id]'


class TipoGastoSerializer(ModelSerializer):
    class Meta:
        model = TipoGasto
        fields = ['id','nome']
        identifier = 'id'
        identifiers = ['id']


class UsuarioSerializer(ModelSerializer):
    gastos = HyperlinkedRelatedField(view_name='gastos_detail', many=True, read_only=True)
    class Meta:
        model = Usuario
        fields = ['gastos','id','nome','data_nascimento','email','senha']
        identifier = 'id'
        identifiers = '[id]'




serializers_dict = {}