import logging

from channels.generic.websocket import AsyncJsonWebsocketConsumer

logger = logging.getLogger(__name__)

class PingConsumer(AsyncJsonWebsocketConsumer):
    group_name = "ping_group"

    async def connect(self):
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
        await self.send_json({"message": "connected"})

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive_json(self, content, **kwargs):
        # Log
        logger.info(f"{self.__class__.__name__} received message", extra={
            "path": self.scope.get("path"),
            "client": self.scope.get("client"),
            "payload_keys": list(content.keys()),
        })

        # Broadcast to group
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "broadcast_message",
                "content": content,
            }
        )

    async def broadcast_message(self, event):
        await self.send_json({
            "broadcast": event["content"]
        })
