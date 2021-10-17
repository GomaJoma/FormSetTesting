from django.db import models


class Examination(models.Model):
    title = models.CharField(max_length=20)
    mark = models.IntegerField(default=0)
    limitations = models.CharField(max_length=50)
    plan_file = models.FileField(upload_to='plans')

    def __str__(self):
        return self.title


class Employer(models.Model):
    lastname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    punishment = models.CharField(max_length=20)
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE)

    def __str__(self):
        return self.lastname


class File(models.Model):
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE)
    data = models.FileField(upload_to='files')

    def __str__(self):
        return str(self.examination)
