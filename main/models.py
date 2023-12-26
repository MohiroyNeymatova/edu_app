from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    status = models.IntegerField(choices=(
        (1, 'waiting'),
        (2, 'in_group')
    ), default=1)
    is_payed = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name


class Direction(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Group(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    money = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.student.first_name