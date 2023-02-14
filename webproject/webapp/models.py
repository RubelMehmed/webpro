from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(verbose_name='Dept Name', max_length=37)

    def __str__(self):
        return self.name


class Course(models.Model):
    c_id = models.PositiveSmallIntegerField(verbose_name='Course Id')
    c_name = models.CharField(verbose_name='Course Name', max_length=30)
    c_duration = models.PositiveSmallIntegerField(verbose_name='Duration')

    def __str__(self):
        return self.c_name


class Teacher(models.Model):
    t_id = models.PositiveSmallIntegerField(verbose_name='Teacher Id')
    t_name = models.CharField(verbose_name='Teacher Name', max_length=25)
    t_sub = models.ForeignKey(Course, on_delete=models.CASCADE)
    t_join = models.DateTimeField(auto_now_add=True, verbose_name='Join Date')
    t_course = models.CharField(max_length=30, verbose_name='District')
    t_department = models.ManyToManyField(Department)
    t_rating = models.DecimalField(
        max_digits=3, decimal_places=2, verbose_name='Rating')

    def __str__(self):
        return self.t_name

    # def __str__(self) -> str:
    #     return super().__str__()
