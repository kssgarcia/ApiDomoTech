import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer 
from api.models import TurnLight
from api.serializers import TurnLightSerializer


class ConsumerAsyn(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'Santiago'
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        print(event)
        dict_lights = {}
        lights = await self.getLight()
        serialize_data = (await self.serializeData(lights)).data
        for i in range(2):
            dict_lights[serialize_data[i]['name']] = serialize_data[i]['stateint']
        await self.send(text_data=json.dumps(dict_lights))

    @sync_to_async
    def getLight(self):
        return list(TurnLight.objects.all())

    @sync_to_async
    def serializeData(self, data):
        return TurnLightSerializer(data, many=True)

    
