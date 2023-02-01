from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course_name}"

class City(models.Model):
    city_name=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city_name}"

class Trainer_reg(models.Model):
    tname = models.CharField(max_length=50)
    tage = models.IntegerField()
    tphno = models.BigIntegerField()
    password = models.CharField(max_length=50,default=None)
    city = models.ForeignKey(City,on_delete=models.CASCADE,default=None)
    def __str__(self):
        return self.tname
    def __str(self):
        return f"{self.tname} ,{self.tage},{self.tphno},{self.city}"

class Trainer_Assign(models.Model):
    t_name = models.ForeignKey(Trainer_reg,on_delete=models.CASCADE,default=None)
    batch_no = models.IntegerField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE,default=None)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.date},{self.batch_no}"