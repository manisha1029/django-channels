from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer
import json
from time import sleep

class MyAsyncConsumer(WebsocketConsumer):
    def connect(self):
        print('Async websocket connected...')
        self.accept()
        # Send a welcome message
        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'Async WebSocket Connected Successfully!'
        }))

    def disconnect(self, close_code):
        print('Async websocket disconnected...')

    def receive(self, text_data):
        print(f'Async received: {text_data}')
        # Send back a response
        for i in range(10):
            self.send(text_data=json.dumps({
                'type': 'message',
                'message': f'Data received: {i}'
            }))
            sleep(1)