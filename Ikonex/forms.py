from django import forms
from .models import Student, Subject, Assessment, ClassStream

class StreamForm(forms.ModelForm):
    class Meta:
        model = ClassStream
        fields = "__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()

        cat = cleaned_data.get("cat_score")
        exam = cleaned_data.get("exam_score")

        if cat is not None:
            if cat > 30:
                raise forms.ValidationError(
                    "Cat score cannot exceed 30"
                )
            
        if exam is not None:
            if exam > 70:
                raise forms.ValidationError(
                    "Exam score cannot exceed 30"
                )
            
        if cat is not None and exam is not None:    
            if cat + exam > 100:
                raise forms.ValidationError(
                    "Cat and exam score cannot exceed 100"
                )
        
        return cleaned_data

