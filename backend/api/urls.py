import re
from django.urls import include, re_path
from rest_framework.routers import DefaultRouter
from .views import *

routerv1 = DefaultRouter()


routerv1.register('default', DefaultViewSet)


urlpatterns = [
    re_path('^', include(routerv1.urls)),
]