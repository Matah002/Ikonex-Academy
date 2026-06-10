from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .models import ClassStream, Assessment, GradeScale, Student, Subject
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import StudentForm, StreamForm, AssessmentForm
from .utils import rank_students, average_score

def dashboard(request):
    students = Student.objects.all()
    rankings = [
        {
            'student' : s,
            'average': average_score(s)
        }
        for s in students
    ]
    rankings = sorted(rankings, key=lambda x: x["average"], reverse=True)
    total_students = students.count()
    total_subjects = Subject.objects.count()
    total_classes = ClassStream.objects.count()
    classes = ClassStream.objects.all()


    overall_average = round(
        sum(average_score(s) for s in students) / total_students
        if total_students else 0,
        2
    )

    context = {
        "total_students": total_students,
        "total_subjects": total_subjects,
        "total_classes": total_classes,
        "overall_average": overall_average,
        'classes': classes,
        "rankings": rankings[:10],
       
        
    }

    return render(request, "home/homepage.html", context)


def class_perfomance(request, class_id):
    class_stream = get_object_or_404(ClassStream, id=class_id)
    students = Student.objects.filter(class_stream=class_stream)

    ranked_list = []

    for student in students:
        assessments = Assessment.objects.filter(student=student)

        subjects_data = {}

        for p in assessments:
            subjects_data[p.subject.name] = {
                'cat': p.cat_score,
                'exam': p.exam_score,
                'total': p.total_score
            }

        avg = average_score(student)

        ranked_list.append({
            "student": student,
            "subjects": subjects_data,
            "average": avg
        })

    ranked_list.sort(key=lambda x: x["average"], reverse=True)

    for index, item in enumerate(ranked_list, start=1):
        item["rank"] = index

    return render(request, "performance/class_performance.html", {
        "class_stream": class_stream,
        "ranked_list": ranked_list,
    })

def class_students(request, class_id):
    class_stream = get_object_or_404(ClassStream, id=class_id)
    students = Student.objects.filter(class_stream = class_stream)
    total_students = students.count()

    

    return render(request, 'students/class_students.html', {
        'students': students,
    })


class StudentListView(ListView):
    model = Student
    template_name = "students/student_list.html"

class AssessmentListView(ListView):
    model = Assessment
    template_name = "assessments/assessment_list.html"

class StreamListView(ListView):
    model = ClassStream
    template_name = "streams/stream_list.html"

class SubjectListView(ListView):
    model = Subject
    template_name = "subjects/subject_list.html"

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name =  "students/student_form.html"
    success_url = reverse_lazy("student-list")

class AssessmentCreateView(CreateView):
    model = Assessment
    form_class = AssessmentForm
    template_name = "assessments/assessment_form.html"
    success_url = reverse_lazy("assessment-list")

class StreamCreateView(CreateView):
    model = ClassStream
    form_class = StreamForm
    template_name = "streams/stream_form.html"
    success_url = reverse_lazy("stream-list")

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name =  "students/student_form.html"
    success_url = reverse_lazy("student-list")

class AssessmentUpdateView(UpdateView):
    model = Assessment
    form_class = AssessmentForm
    template_name = "assessments/assessment_form.html"
    success_url = reverse_lazy("assessment-list")

class StreamUpdateView(UpdateView):
    model = ClassStream
    form_class = StreamForm
    template_name = "streams/stream_form.html"
    success_url = reverse_lazy("stream-list")

class StudentDeleteView(DeleteView):
    model = Student
    template_name = "students/student_confirm_delete.html"
    success_url = reverse_lazy("student-list")

class AssessmentDeleteView(CreateView):
    model = Assessment
    form_class = AssessmentForm
    template_name = "assessments/assessment_confirm_delete.html"
    success_url = reverse_lazy("assessment-list")

class StreamDeleteteView(CreateView):
    model = ClassStream
    template_name = "streams/stream_confirm_delete.html"
    success_url = reverse_lazy("stream-list")