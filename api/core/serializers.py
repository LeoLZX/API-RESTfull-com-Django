from rest_framework import serializers
from .models import Produtos

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = ('id', 'codigo', 'descricao','preco')