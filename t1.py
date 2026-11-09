
import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restdj.settings')
django.setup(set_prefix=False)

from quickstart.models import Employee


from quickstart.serializers import EmployeeSerializer

mgr = Employee.objects.using('default')

# 序列化： ==> 响应阶段
# 1. 类型转换，将json不支持的数据类型转为支持的
# 2. 序列化，将python对象转为字符串
# instance = mgr.get(pk=10004)
instance = mgr.last()
serializer = EmployeeSerializer(instance)
print(serializer.data, type(serializer.data))

# 反序列化  <== 入库阶段
# 1. json str => dict|list|object
# 2. 入库
data = {'emp_no': 10021, 'birth_date': '1992-01-08', 'first_name': 'Deng', 'last_name': 'You', 'gender': 1, 'hire_date': '1992-01-26'}
serializer = EmployeeSerializer(data=data)

if serializer.is_valid():
#     print(serializer.validated_data)
    serializer.save()

