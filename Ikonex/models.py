from django.db import models

# Create your models here.
class ClassStream(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    class_stream = models.ForeignKey(ClassStream, on_delete=models.CASCADE, related_name="students")
    admission_number = models.CharField(max_length=40, unique=True)
    surname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.admission_number} - {self.first_name}"
    
class Subject(models.Model):
    name = models.CharField(max_length=50)
    subject_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class ClassSubject(models.Model):
    class_stream = models.ForeignKey(ClassStream, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('class_stream', 'subject')

class GradeScale(models.Model):
    grade = models.CharField(max_length=5)
    min_score = models.FloatField()
    max_score = models.FloatField()

    def __str__(self):
        return self.grade
    
class Assessment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # grade = models.ForeignKey(GradeScale, on_delete=models.CASCADE)
    cat_score = models.FloatField(default=0)
    exam_score = models.FloatField(default=0)

    class Meta:
        unique_together = ('student', 'subject')

    @property
    def total_score(self):
        return self.cat_score + self.exam_score

