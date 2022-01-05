from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User, Student, Professor
from PIL import Image

class StudentSignUpForm(UserCreationForm):
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    rollno = forms.CharField(max_length=15)
    emailid = forms.EmailField(max_length=100)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        fnm = self.cleaned_data['firstname']
        lnm = self.cleaned_data['lastname']
        eid = self.cleaned_data['emailid']
        rno = self.cleaned_data['rollno']
        user.firstname = fnm
        user.lastname = lnm
        user.emailid = eid
        user.rollno = rno
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.firstname = fnm
        student.lastname = lnm
        student.emailid = eid
        student.rollno = rno
        student.save()
        return user

class ProfessorSignUpForm(UserCreationForm):
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    staffid = forms.CharField(max_length=15)
    emailid = forms.EmailField(max_length=30)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        fnm = self.cleaned_data['firstname']
        lnm = self.cleaned_data['lastname']
        eid = self.cleaned_data['emailid']
        sid = self.cleaned_data['staffid']
        user.firstname = fnm
        user.lastname = lnm
        user.emailid = eid
        user.staffid = sid
        user.is_professor = True
        user.save()
        prof = Professor.objects.create(user=user)
        prof.firstname = fnm
        prof.lastname = lnm
        prof.emailid = eid
        prof.staffif = sid
        return user
    
class StudentUpdateForm(forms.ModelForm):
    rollno = forms.CharField(max_length=15, label="Roll No")
    firstname = forms.CharField(max_length=50, label="First Name")
    lastname = forms.CharField(max_length=50, label="Last Name")
    emailid = forms.EmailField(label="Email ID")
    image = forms.ImageField(label="Image")

    class Meta:
        model = User
        fields = ["firstname", "lastname", "emailid", "rollno", "image"]