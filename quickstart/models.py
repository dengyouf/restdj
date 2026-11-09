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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
"""


class Employee(models.Model):
    class Meta:
        db_table = 'employees'
        verbose_name = '书籍'
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

    def __str__(self):
        return f"<{self.emp_no} {self.birth_date} {self.first_name} {self.last_name}>"

