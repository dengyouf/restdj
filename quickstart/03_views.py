"""
Concrete View
"""

from quickstart.models import Employee
from quickstart.serializers import EmployeeSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView



class EmpsView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmpView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer






