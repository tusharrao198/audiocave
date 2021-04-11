import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        print("Join room_group_name", self.room_group_name)
        await self.accept()

    async def disconnect(self, close_code):
        print("# Leave room group")
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        
    # Receive message from WebSocket
    async def receive(self, text_data):
        json_recieved = json.loads(text_data)
        data = {}
        data["type"] = "chat_message"
        for i in list(json_recieved.keys()):
            data[i] = json_recieved[i]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            data,
        )

    # Receive message from room group
    async def chat_message(self, event):
        # print("event",event)

        data_received = {}
        for i in list(event.keys()):
            data_received[i] = event[i]
        print("data_recieved", data_received,"\n")

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps(data_received)
        )
