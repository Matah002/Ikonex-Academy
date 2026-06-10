from django.urls import path
from .views import *
from .reports import student_report_card_pdf


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('classstudents/<int:class_id>/', class_students, name='class-students'),
    path("students/", StudentListView.as_view(), name="student-list"),
    path("assessments/", AssessmentListView.as_view(), name="assessment-list"),
    path("streams/", StreamListView.as_view(), name='stream-list'),
    path("subjects/", SubjectListView.as_view(), name="subject-list"),
    path("students/create/", StudentCreateView.as_view(), name="student-create"),
    path("assessments/create", AssessmentCreateView.as_view(), name="assessment-create"),
    path("streams/create", StreamCreateView.as_view(), name='stream-create'),
    path("students/<int:pk>/update/", StudentUpdateView.as_view(), name="update-student"),
    path("assessments/<int:pk>/update/", AssessmentUpdateView.as_view(), name="update-assessment"),
    path("streams/<int:pk>/update/", StreamUpdateView.as_view(), name='update-stream'),
    path("assessments/<int:pk>/delete/", AssessmentDeleteView.as_view(), name="delete-assessment"),
    path("students/<int:pk>/delete/", StudentDeleteView.as_view(), name="delete-student"),
    path("streams/<int:pk>/delete/", StreamUpdateView.as_view(), name='delete-stream'),
    path('classes/<int:class_id>/performance/', class_perfomance, name='class-performance'),
    path('students/<int:student_id>/report-card/', student_report_card_pdf, name='student-report-card-pdf')
]
