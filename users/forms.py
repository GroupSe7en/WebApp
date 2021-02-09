from django import forms
from .models import StudentProfile, LecturerProfile

class StudentProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['firstName', 'lastName', 'indexNo', 'department', 'contactNo', 'image']

class LecturerProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = LecturerProfile
        fields = ['firstName', 'lastName', 'department', 'image']