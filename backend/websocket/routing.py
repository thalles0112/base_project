from django.urls import re_path

ASYNC = True


from . import consumers_async
from . import consumers_sync


consumers = consumers_sync

if ASYNC:
    consumers = consumers_async
else:
    consumers = consumers_sync



websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]