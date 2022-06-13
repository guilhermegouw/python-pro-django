from django.urls import path
from .views import video


app_name = 'aperitivos'

urlpatterns = [
    path('<slug:slug>', video, name='video'),
]
