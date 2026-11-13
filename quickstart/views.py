from rest_framework import status
from rest_framework.request import Request

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from quickstart.models import Employee
from quickstart.serializers import EmployeeSerializer

from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin,
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
)

from utils.paginations import CustomerPageNumberPagination

# class EmpsView(ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#     # pagination_class = None # 为None则调用全局的
#     pagination_class = CustomerPageNumberPagination #
#
#
#
# class EmpView(RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


class EmpViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomerPageNumberPagination



