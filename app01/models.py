from django.db import models


# Create your models here.

# 用户列表
class User(models.Model):
    id = models.AutoField(primary_key=True)  # 自增ID
    email = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

    def __str__(self):
        return self.email


# 出版社列表
class Press(models.Model):
    id = models.AutoField(primary_key=True)  # 自增ID
    press_name = models.CharField(max_length=32)


# 书籍列表
class Book(models.Model):
    id = models.AutoField(primary_key=True)  # 自增ID
    book_name = models.CharField(max_length=32)
    # Django 1.11默认就是级联删除，Django 2.0之后必须指定on_delete,to=关联的表明
    press = models.ForeignKey(to='Press', on_delete=models.CASCADE)


# 作者列表
class Author(models.Model):
    id = models.AutoField(primary_key=True)  # 自增ID
    author_name = models.CharField(max_length=32)

    books = models.ManyToManyField(to='Book')  # 多对多，会多创建一张表
