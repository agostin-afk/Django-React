from rest_framework import serializers
from Unidades.models import Unidade,SubUnidade

class SubUnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubUnidade
        exclude = ['id']
    
class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = '__all__'