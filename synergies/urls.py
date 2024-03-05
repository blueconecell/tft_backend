from django.urls import path

from . import views

urlpatterns = [
    path("origins",views.OriginList.as_view()),
    path("jobs",views.JobList.as_view()),
]
