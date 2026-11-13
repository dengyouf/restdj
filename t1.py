
import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restdj.settings')
django.setup(set_prefix=False)

from quickstart.models import Employee


from quickstart.serializers import EmployeeSerializer, SalarySerializer

mgr = Employee.objects.using('default')

# 序列化： ==> 响应阶段
# 1. 类型转换，将json不支持的数据类型转为支持的
# 2. 序列化，将python对象转为字符串
# instance = mgr.get(pk=10004)
# # print(instance.salary_set.all())
# print(instance.salarys.all())
# # instance = mgr.last()
# serializer = EmployeeSerializer(instance=instance)
# print(serializer.data)


# 反序列化  <== 入库阶段
# 1. json str => dict|list|object
# 2. 入库
# data = {
#     'emp_no': 10025,
#     'birth_date': '1992-01-08',
#     'first_name': 'Ding',
#     'last_name': 'Yuanyuan',
#     'gender': 0,
#     'hire_date': '1988-01-26'
# }
# #  新增
# serializer = EmployeeSerializer(data=data)
# if serializer.is_valid(raise_exception=True):
#     # print(serializer.validated_data)
#     serializer.save()

# 更新
# emp = mgr.get(pk="10020")
# serializer = EmployeeSerializer(instance=emp, data=data)
# if serializer.is_valid(raise_exception=True):
#     serializer.save()


# 1对多 ， 序列化
emp = Employee.objects.get(pk=10001)
print(emp)
print(emp.salaries.all())
################ 分别查询
# print("+"*50)
# print(EmployeeSerializer(instance=emp).data)
# print(SalarySerializer(instance=emp.salaries.all(), many=True).data)
# print("+"*50)
############### 一次查询出来
# 在多的一列添加新的字段，并且在fileds追加这个字段
# salaries = serializers.StringRelatedField(many=True)
#     salaries = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
# fields.append("salaries")
print("-"*50)
print(EmployeeSerializer(instance=emp).data)
print("-"*50)