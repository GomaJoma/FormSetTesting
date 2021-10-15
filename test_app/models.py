from django.db import models


class Employer(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    punishment = models.CharField(max_length=20)

    def __str__(self):
        return self.lastname


class File(models.Model):
    data = models.FileField()

    def __str__(self):
        return self.id


class Examination(models.Model):
    title = models.CharField(max_length=20)
    mark = models.IntegerField()
    limitations = models.CharField(max_length=50)
    plan_file = models.FileField()
    employees = models.ForeignKey(Employer, on_delete=models.CASCADE)
    files = models.ForeignKey(File, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
