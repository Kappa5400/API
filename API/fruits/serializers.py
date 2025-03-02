from rest_framework import serializers
from .models import fruit

class fruitserial(serializers.ModelSerializer):
    class Meta:
        model = fruit
        fields = ('id', 'name', 'rank', 'comment')
