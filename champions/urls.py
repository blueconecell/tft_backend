from . import views
from django.urls import path

urlpatterns = [
    path("",views.Champions.as_view()),
    path("<int:pk>",views.ChampionDetails.as_view())
]