from .models import Assessment, GradeScale, Student
# Create your views here.

def average_score(student):
    assessments = Assessment.objects.filter(student=student)
    total = sum(p.total_score for p in assessments)
    count = assessments.count()

    return total / count if count else 0


def determine_grade(score):
    grade = GradeScale.objects.filter(min_score__lte=score, max_score__gte=score).first()
    return grade.grade if grade else "N/A"


def rank_students(class_stream):
    students = Student.objects.filter(class_stream=class_stream)

    ranked = []

    for student in students:
        ranked.append({
            "student":student,
            "average": average_score(student)
        })

    ranked.sort(key=lambda x: x["average"], reverse=True)

    return ranked