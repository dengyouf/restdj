"""
GenericAPI 视图
"""

from rest_framework.request import Request

from rest_framework.response import Response

from quickstart.models import Employee
from quickstart.serializers import EmployeeSerializer

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin,
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
)


class EmpsView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # get， post => list, create
    def get(self, request: Request) -> Response:
        return self.list(request)
    def post(self, request: Request) -> Response:
        return self.create(request)

class EmpView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # get， put, patch, delete  => list, update, delete
    def get(self, request: Request, *args, **kwargs) -> Response:
        return self.retrieve(request,  *args, **kwargs)
    def put(self, request: Request, *args, **kwargs) -> Response:
        return self.update(request, *args, **kwargs)
    def patch(self, request: Request, *args, **kwargs) -> Response:
        return self.partial_update(request, *args, **kwargs)
    def delete(self, request: Request ,*args, **kwargs) -> Response:
        return self.destroy(request , *args, **kwargs)





