from django.urls import path
from Mean_A1.views import calculate


app_name = "Mean_AA"

urlpatterns = [
    path("calculate", calculate, name = "calculate"),
]