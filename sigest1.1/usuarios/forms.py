from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario,Student,Advisor,Supervisor
from django.db import transaction
from django.shortcuts import redirect



class StudentSignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('first_name', 'username', 'email', 'matricula')

    @transaction.atomic

    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user




class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('first_name', 'username', 'email', 'matricula')

    @transaction.atomic

    def update_student(request):

            try:
                student = request.user.student

            except Student.DoesNotExist:

                student = Student(user=request.user)

            if request.method == 'POST':
                form = StudentUpdateForm(request.POST, instance=student)
                if form.is_valid():
                    form.save
                    return redirect('student_list')
                else:
                    form = StudentUpdateForm(instance=student)
                    return render('student_list')






class AdvisorSignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('first_name', 'username', 'email', 'matricula')

    @transaction.atomic

    def save(self):
        user = super().save(commit=False)
        user.is_advisor = True
        user.save()
        advisor = Advisor.objects.create(user=user)
        return user



class AdvisorUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email','matricula','is_active')

    @transaction.atomic

    def update_advisor(request):

            try:
                advisor = request.user.advisor

            except Advisor.DoesNotExist:

                advisor = Advisor(user=request.user)

            if request.method == 'POST':
                form = AdvisorUpdateForm(request.POST, instance=advisor)
                if form.is_valid():
                    form.save
                    return redirect('advisor_list')
                else:
                    form = AdvisorUpdateForm(instance=student)
                    return render('advisor_list')







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




class SupervisorUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email','matricula','is_active')

    @transaction.atomic

    def update_supervisor(request):

            try:
                supervisor = request.user.supervisor

            except Supervisor.DoesNotExist:

                supervisor = Supervisor(user=request.user)

            if request.method == 'POST':
                form = Supervisor(request.POST, instance=supervisor)
                if form.is_valid():
                    form.save
                    return redirect('supervisor_list')
                else:
                    form = SupervisorUpdateForm(instance=supervisor)
                    return render('supervisor_list')


