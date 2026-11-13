from django.db import models

# Create your models here.
"""
CREATE TABLE `employees` (
  `emp_no` int NOT NULL,
  `birth_date` date NOT NULL,
  `first_name` varchar(14) NOT NULL,
  `last_name` varchar(16) NOT NULL,
  `gender` smallint NOT NULL DEFAULT '1' COMMENT 'M=1, F=2',
  `hire_date` date NOT NULL,
  PRIMARY KEY (`emp_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

class TestManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().using("default")
class AbstractModelBase(models.Model):
    objects = models.Manager()
    class Meta:
        abstract = True


class Employee(AbstractModelBase):
    # objects = TestManager()

    class Meta:
        db_table = 'employees'
        verbose_name = '员工'
        verbose_name_plural = 'employees'
    class Gender(models.IntegerChoices):
        FEMALE = 0, "女"
        MALE = 1, "男"
    emp_no = models.IntegerField(primary_key=True, null=False, unique=True, verbose_name="工号")
    birth_date = models.DateField(null=False, verbose_name="生日")
    first_name = models.CharField(max_length=14, verbose_name="姓")
    last_name = models.CharField(max_length=16, verbose_name="名")
    gender = models.SmallIntegerField(choices=Gender.choices, default=Gender.MALE, verbose_name="性别")
    hire_date = models.DateField(null=False)

    @property
    def username(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f"<{self.emp_no} {self.birth_date} {self.username}>"

    __repr__ = __str__

"""
CREATE TABLE `salaries` (
  `emp_no` int NOT NULL,
  `salary` int NOT NULL,
  `from_date` date NOT NULL,
  `to_date` date NOT NULL,
  `id` bigint NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `emp_no` (`emp_no`),
  CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) REFERENCES `employees` (`emp_no`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb3;
"""
class Salary(AbstractModelBase):
    class Meta:
        db_table = 'salaries'
        verbose_name = '薪资'
        verbose_name_plural = 'salaries'
    id = models.BigAutoField(primary_key=True, db_column='id')
    #  emp_no
    emp_no = models.ForeignKey(
        "Employee",
        on_delete=models.CASCADE,
        db_column='emp_no',
        related_name="salaries"
    )
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()


    def __str__(self):
        return f"<{self.emp_no} {self.salary}>"
    __repr__ = __str__


# print("="*50)
# print(*Employee.__dict__.items(), sep="\n")
# print(*Salary.__dict__.items(), sep="\n")
# print("="*50)