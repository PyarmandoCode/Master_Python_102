from django.db import models

# class Book(models.Model):
#     title=models.CharField(max_length=100)
#     author=models.CharField(max_length=100)
#     publish_date=models.DateField()
#     isbn=models.CharField(max_length=13,unique=True)
#     price=models.DecimalField(max_digits=5,decimal_places=2)

#     def __str__(self):
#         return self.title

class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth=models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Profile(models.Model):
    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    bio=models.TextField()
    avatar=models.ImageField(upload_to='avatars/',null=True,blank=True)

    def __str__(self):
        return f'Perfil de {self.student.first_name}'
    
class Teacher(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    hire_date=models.DateField()

    def __str__(self):
        return f'Profesor {self.first_name} {self.last_name}'
    
class Course(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='courses')
    students=models.ManyToManyField(Student,related_name='courses')

    def __str__(self):
        return self.name
    
class Grade(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='grades')
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='grades')
    score=models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return f'{self.student.first_name} {self.student.last_name} - {self.course.name}:{self.score}'

