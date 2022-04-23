from django.db import models
from django.contrib.auth.models import User


class Classes(models.Model):
    # 请根据题目说明自行补全完整的Model
    name = models.CharField('班级名称', max_length=8, unique=True,   null=False)


class Student(models.Model):
    # 请根据题目说明自行补全完整的Model
    user = models.OneToOneField(User,
        db_constraint=False,
        on_delete=models.CASCADE,
        null=True
    )

    sex = models.SmallIntegerField('性别')

    owner_class = models.ForeignKey(
        Classes,
        verbose_name='班级',
        related_name='students',
        on_delete=models.SET_NULL,
        null=True
    )
