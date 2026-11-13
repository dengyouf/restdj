from django.shortcuts import render

# Create your views here.
from django.contrib import admin
from django.urls import path, include
# from .views import  EmpView,EmpsView

from .views import  EmpViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', EmpViewSet)

urlpatterns = []+router.urls

# urlpatterns = [
#     # path("", EmpsView.as_view(), name="emps"),
#     # path("<int:pk>/", EmpView.as_view(), name="emp"),
#
#     path("", EmpViewSet.as_view({"get": "list", "post": "create"})),
#     path("<int:pk>/", EmpViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"})),
# ]