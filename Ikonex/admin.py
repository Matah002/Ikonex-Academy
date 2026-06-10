from django.contrib import admin
from .models import ClassStream, ClassSubject, Assessment, GradeScale, Student, Subject
# Register your models here.

class student(admin.ModelAdmin):
    list_display = ('class_stream','admission_number', 'surname', 'first_name', 'last_name', 'created_at')
    list_filter = ('class_stream',)
    search_fields =('admission_number',)

class classstream(admin.ModelAdmin):
    list_display = ('name',)

class subject(admin.ModelAdmin):
    list_display = ('name', 'subject_code')

class classsubject(admin.ModelAdmin):
    list_display = ('class_stream', 'subject')

class gradescale(admin.ModelAdmin):
    list_display = ('grade', 'min_score', 'max_score')

class assessment(admin.ModelAdmin):
    list_display = ('subject', 'student', 'cat_score', 'exam_score')

admin.site.register(Student, student)
admin.site.register(ClassStream, classstream)
admin.site.register(Subject, subject)
admin.site.register(ClassSubject, classsubject)
admin.site.register(GradeScale, gradescale)
admin.site.register(Assessment, assessment)

