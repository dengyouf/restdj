
# https://www.django-rest-framework.org/api-guide/serializers/


from rest_framework import serializers

from .models import Employee

# 公共函数
# def validate_name(field_name, value):
#     if len(value) <= 3 or len(value) >= 14:
#         raise serializers.ValidationError(f"{field_name}长度在4～14之间")
#     return value
import functools
def validate_name(value, field_name="firt_name", mi=4, mx=14):
    if len(value) < mi or len(value) > mx:
        raise serializers.ValidationError(f"{field_name}长度在{mi}～{mx}之间")
    return value

class EmployeeSerializer(serializers.Serializer):
    emp_no = serializers.IntegerField()
    birth_date = serializers.DateField()
    first_name = serializers.CharField(validators=[validate_name])
    # last_name = serializers.CharField(min_length=3, max_length=14)
    last_name = serializers.CharField(validators=[functools.partial(validate_name, field_name="last_name",mi=2, mx=8)])
    gender = serializers.ChoiceField(choices=Employee.Gender.choices)
    hire_date = serializers.DateField()

    # 字段级校验器
    # def validate_first_name(self, value):
    # #     if len(value) <= 4 or len(value) >= 14:
    # #         raise serializers.ValidationError("长度在4～14之间")
    # #     return value
    #     return validate_name("fast_name", value)
    # def validate_last_name(self, value):
    # #     return  self.validate_first_name(value)
    #     return validate_name("last_name", value)

    # 对象级别校验器
    # def validate(self, attrs:dict):
    #     print("*"*50)
    #     print(attrs.get("first_name"))
    #     value = attrs.get("first_name")
    #     if len(value) < 4 or len(value) > 14:
    #         raise serializers.ValidationError("长度在4～14之间")
    #     print("*"*50)
    #     return attrs


    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.birth_date = validated_data.get("birth_date", instance.birth_date)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.gender = validated_data.get("gender", instance.gender)
        instance.hire_date = validated_data.get("hire_date", instance.hire_date)
        instance.save()
        return instance



print("*" * 50)
print(EmployeeSerializer())
print("*" * 50)
