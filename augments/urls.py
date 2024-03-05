from django.urls import path

from . import views

urlpatterns = [
    path("",views.AugmentList.as_view()),
]
