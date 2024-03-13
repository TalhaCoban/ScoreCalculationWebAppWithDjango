from django.urls import path
from LGS.views import calculate, SaveResults, dashboard, DeleteResult, SureToDeleteResult


app_name = "LGS"

urlpatterns = [
    path("calculate/<int:id>", calculate, name = "calculate"),
    path("SaveResults/<int:id>", SaveResults, name="SaveResults"),
    path("dashboard/<int:id>", dashboard, name = "dashboard"),
    path("DeleteResult/<int:id>", DeleteResult, name = "DeleteResult"),
    path("SureToDeleteResult/<int:id>", SureToDeleteResult, name = "SureToDeleteResult"),
]