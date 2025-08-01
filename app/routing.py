from django.urls import path
from .consumers import MyAsyncConsumer

websocket_urlpatterns = [
    path("ws/ac/", MyAsyncConsumer.as_asgi()),
]