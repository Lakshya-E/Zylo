from django.urls import path, include
from .views import intro, RoomView

urlpatterns = [
    path('intro', intro),
    path('room', RoomView.as_view()),
]
