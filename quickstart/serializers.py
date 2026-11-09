from rest_framework import serializers

from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    emp_no = serializers.IntegerField(read_only=True)
    birth_date = serializers.DateField()
    first_name = serializers.CharField(max_length=14)
    last_name = serializers.CharField(max_length=16)
    gender = serializers.ChoiceField(choices=Employee.Gender.choices)
    hire_date = serializers.DateField()

    def create(self, validated_data):
        return Employee(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance

    def save(self, **kwargs):
        print(kwargs)


print("*" * 50)
print(EmployeeSerializer())
print("*" * 50)
