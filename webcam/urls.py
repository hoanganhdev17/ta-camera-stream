from django.urls import path
from .views import index, live_stream


urlpatterns = [
    path('', index, name='index'),
    path('live_stream/', live_stream, name='live-stream'),
]