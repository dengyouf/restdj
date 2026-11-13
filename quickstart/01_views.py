"""
APIView 视图
"""

from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response

from quickstart.models import Employee
from quickstart.serializers import EmployeeSerializer

class EmpsView(APIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        return self.queryset
    def get_serializer_class(self):
        return self.serializer_class
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        return serializer_class(*args, **kwargs) # EmployeeSerializer()
    def get(self, request):
        serializer = self.get_serializer(inistance=self.queryset(), many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
class EmpView(APIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        return self.queryset
    def get_serializer_class(self):
        return self.serializer_class
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        return serializer_class(*args, **kwargs)  # EmployeeSerializer()
    def get_object(self):
        lookup_key = 'pk'
        return self.queryset.get(pk=self.kwargs[lookup_key])

    def get(self, request, pk=None):
        # instance = Employee.objects.all().get(pk=pk)
        # serializer = EmployeeSerializer(instance)
        # return Response(serializer.data)
        # instance = self.queryset.get(pk=pk)
        instance = self.get_object()
        return Response(self.get_serializer(instance).data)
    def put(self, request, pk=None):
        # instance = Employee.objects.all().get(pk=pk)
        # serializer = EmployeeSerializer(instance, data=request.data)
        # print(serializer.is_valid())
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()
        #     return Response(serializer.data,status=status.HTTP_201_CREATED)

        # instance = self.queryset.get(pk=pk)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk=None):
        # instance = Employee.objects.all().get(pk=pk)
        # instance.delete()

        # instance = self.queryset.get(pk=pk)
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class TestView(APIView):
    # http://172.16.162.1:8000/emps/?x=123&y=abc
    def get(self, request:Request):
        print("="*50)
        print(request.method) #GET
        print(request.GET)
        print(request.GET.get("y"))
        print(request.query_params)
        print(request.query_params.get("x"))
        print("="*50)
        return Response({'message': 'get hello world'})
    def post(self, request:Request):
        print("="*50)
        print(request.method)
        print(request.POST) # form
        print(request.POST.get("name"))
        print(request.data) # json
        print(request.data.get("password"))
        print("="*50)
        data = {'message': 'post hello world'}
        headers = {'X-server': 'my/python'}
        return Response(data=data, status=status.HTTP_200_OK, headers=headers)