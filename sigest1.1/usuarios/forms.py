from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario,Student,Advisor,Supervisor
from django.db import transaction




class StudentSignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('username', 'email','matricula','is_active' )

    @transaction.atomic

    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user


class AdvisorSignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('username', 'email', 'matricula')

    @transaction.atomic

    def save(self):
        user = super().save(commit=False)
        user.is_advisor = True
        user.save()
        advisor = Advisor.objects.create(user=user)
        return user




class SupervisorSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('username', 'email', 'matricula')

    @transaction.atomic

    def save(self):
        user = super().save(commit=False)
        user.is_supervisor = True
        user.save()
        supervisor = Supervisor.objects.create(user=user)
        return user