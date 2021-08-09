from django.urls import path
from . import views

urlpatterns = [
    path("musicapp/", views.SongList.as_view()),
    path("musicapp/<int:pk>/", views.Detail.as_view())
]