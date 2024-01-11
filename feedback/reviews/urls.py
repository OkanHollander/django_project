from django.urls import path
from . import views


urlpatterns = [
    path("", views.reviewer, name="review")
]
