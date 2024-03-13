from django.contrib import admin
from django.urls import path
from YKS.views import calculate, SaveResults, dashboard, DeleteResult, detail, SureToDeleteResult


app_name = "YKS"

urlpatterns = [
    path("calculate/<int:id>", calculate, name = "calculate"),
    path("SaveResults/<int:id>" , SaveResults, name = "SaveResults"),
    path("dashboard/<int:id>", dashboard, name = "dashboard"),
    path("DeleteResult/<int:id>", DeleteResult, name = "DeleteResult"),
    path("detail/<int:id>", detail, name = "detail"),
    path("SureToDeleteResult/<int:id>", SureToDeleteResult, name = "SureToDeleteResult"),
]

