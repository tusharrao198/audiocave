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
        text_data_json = json.loads(text_data)
        # print("DATA received", text_data_json)
        message = text_data_json["message"]
        playPausemessage = text_data_json["playPausemessage"]
        leaveRoom = text_data_json["leaveRoom"]
        updateSong = text_data_json["updateSong"]

        # print("messages", message)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "playPausemessage": playPausemessage,
                "leaveRoom": leaveRoom,
                "updateSong": updateSong,
            },
        )
        print("SEND MESSAGES", self.room_group_name)

    # Receive message from room group
    async def chat_message(self, event):
        # print("event",event)
        data_received = {
            "message": event["message"],
            "playPausemessage": event["playPausemessage"],
            "leaveRoom": event["leaveRoom"],
            "updateSong": event["updateSong"],
        }
        print("data_recieved", data_received,"\n")
        # Send message to WebSocket
        await self.send(
            text_data=json.dumps(data_received)
        )
