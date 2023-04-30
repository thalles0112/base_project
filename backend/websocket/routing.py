from django.urls import re_path

ASYNC = False  



from . import consumers_sync




websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers_sync.ChatConsumer.as_asgi()),
]