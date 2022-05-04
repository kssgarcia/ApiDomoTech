from django.shortcuts import render
from django.http import JsonResponse
from matplotlib.colors import LightSource
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.serializers import Serializer 
from .serializers import CardCodeSerializer, TurnLightSerializer
from .models import TurnLight, CardModel
from chat.consumers import ConsumerAsyn

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@api_view(['GET'])
def getRoute(request):
    ligthStatus = [
        {
            'method': 'GET',
            'state': True,
        },
        {
            'method': 'GET',
            'state': True,
        }
    ]
    return JsonResponse(LightSource)

@api_view(['GET'])
def getLights(request):
    ligthStatus = TurnLight.objects.all()
    serializeData = TurnLightSerializer(ligthStatus, many=True)
    return Response(serializeData.data)


@api_view(['GET'])
def getLight(request, pk):
    ligthStatus = TurnLight.objects.get(id=pk)
    serializeData = TurnLightSerializer(ligthStatus, many=False)
    return Response(serializeData.data)

@api_view(['POST'])
def createLight(request):
    data = request.data
    light = TurnLight.objects.create(
        name = data['name'],
        state = data['state'],
        ip = data['ip'],
    )
    instance = ConsumerAsyn
    instance.receive()
    ConsumerAsyn.receive()
    serializeData = TurnLightSerializer(light, many=False)
    return Response(serializeData.data)

@api_view(['PUT'])
def updateLight(request, pk):
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        'chat_Santiago',
        {
            'type': 'chat_message',
        }
    )

    light = TurnLight.objects.get(id=pk)
    serializeData = TurnLightSerializer(light, data=request.data)
    if serializeData.is_valid():
        serializeData.save()
    return Response(serializeData.data)

@api_view(['DELETE'])
def deleteLight(request, pk):
    light = TurnLight.objects.get(id=pk)
    name = light
    light.delete()
    return Response(f'Light {name} was delete')

@api_view(['GET'])
def getCardCodes(request):
    ligthStatus = CardModel.objects.all()
    serializeData = CardCodeSerializer(ligthStatus, many=True)
    return Response(serializeData.data)

@api_view(['GET'])
def getCardCode(request, pk):
    card = CardModel.objects.get(id=pk)
    serializeData = CardCodeSerializer(card, many=False)
    return Response(serializeData.data)

@api_view(['POST'])
def createCard(request):
    data = request.data
    card = CardModel.objects.create(
        cardCode = data['cardCode'],
    )
    serializeData = CardCodeSerializer(card, many=False)
    return Response(serializeData.data)
