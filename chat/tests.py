from django.test import TestCase

import json
from unittest import TestCase
from unittest.mock import AsyncMock

from chat.consumers import ChatConsumer

class TestChatConsumer(TestCase):
    async def test_receive(self):
        # Create an instance of ChatConsumer
        consumer = ChatConsumer()

        # Mock the send method
        consumer.send = AsyncMock()

        # Simulate receiving a message
        message = {"message": "Test message"}
        text_data = json.dumps(message)
        await consumer.receive(text_data)

        # Ensure that the send method was called with the correct message
        consumer.send.assert_awaited_once_with(text_data=json.dumps(message))

