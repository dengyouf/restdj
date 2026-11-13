# https://www.django-rest-framework.org/tutorial/1-serialization/#using-modelserializers
from rest_framework import serializers
from rest_framework.fields import IntegerField

from .models import Employee,Salary


# 公共函数
# def validate_name(field_name, value):
#     if len(value) <= 3 or len(value) >= 14:
#         raise serializers.ValidationError(f"{field_name}长度在4～14之间")
#     return value
from django.db import models

class SalarySerializer(serializers.ModelSerializer):
    salary = IntegerField(min_value=0)
    class Meta:
        model = Salary
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    # 主键关联：{'emp_no': 10001, 'first_name': 'Georgi', 'last_name': 'Facello', 'gender': 1, 'hire_date': '1986-06-26', 'salaries': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]}
    # salaries = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # 自定义字符串关联 每一个管理instance通过 __str__ 返回值， {'emp_no': 10001, 'first_name': 'Georgi', 'last_name': 'Facello', 'gender': 1, 'hire_date': '1986-06-26', 'salaries': ['<<10001 1953-09-02 Georgi Facello> 60117>', '<<10001 1953-09-02 Georgi Facello> 62102>', '<<10001 1953-09-02 Georgi Facello> 66074>', '<<10001 1953-09-02 Georgi Facello> 66596>', '<<10001 1953-09-02 Georgi Facello> 66961>', '<<10001 1953-09-02 Georgi Facello> 71046>', '<<10001 1953-09-02 Georgi Facello> 74333>', '<<10001 1953-09-02 Georgi Facello> 75286>', '<<10001 1953-09-02 Georgi Facello> 75994>', '<<10001 1953-09-02 Georgi Facello> 76884>', '<<10001 1953-09-02 Georgi Facello> 80013>', '<<10001 1953-09-02 Georgi Facello> 81025>', '<<10001 1953-09-02 Georgi Facello> 81097>', '<<10001 1953-09-02 Georgi Facello> 84917>', '<<10001 1953-09-02 Georgi Facello> 85112>', '<<10001 1953-09-02 Georgi Facello> 85097>', '<<10001 1953-09-02 Georgi Facello> 88958>']}
    # salaries = serializers.StringRelatedField(many=True, read_only=True)

    # salaries = serializers.HyperlinkedRelatedField(many=True, view_name="salay-detail", read_only=True)
    # ， {'emp_no': 10001, 'first_name': 'Georgi', 'last_name': 'Facello', 'gender': 1, 'hire_date': '1986-06-26', 'salaries': [60117, 62102, 66074, 66596, 66961, 71046, 74333, 75286, 75994, 76884, 80013, 81025, 81097, 84917, 85112, 85097, 88958]}
    # 自定义字段
    # salaries = serializers.SlugRelatedField(many=True, read_only=True, slug_field='salary')

    # 嵌入的关系
    # salaries = SalarySerializer(many=True, read_only=True)
    class Meta:
        model = Employee
        # fields = '__all__'
        fields = ["emp_no", "first_name", "last_name", "gender", "birth_date", "hire_date"]
        # fields.append("salaries")
        # read_only_fields = ["emp_no"]
        extra_kwargs = {
            # "birth_date": {"write_only": True},
            "first_name": {"max_length": 14, "min_length": 4},
        }

# print("*" * 50)
# print(EmployeeSerializer())
# print("*" * 50)




print("*" * 50)
print(SalarySerializer())
print("*" * 50)