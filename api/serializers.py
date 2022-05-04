from rest_framework.serializers import ModelSerializer
from .models import CardModel, TurnLight


class TurnLightSerializer(ModelSerializer):
    class Meta:
        model = TurnLight
        fields = '__all__'


class CardCodeSerializer(ModelSerializer):
    class Meta:
        model = CardModel
        fields = '__all__'
