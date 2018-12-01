from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DetailView

from usuarios.forms import StudentUpdateForm
from ..models import Usuario,Student
from ..forms import StudentSignupForm
from django.contrib import messages

class StudentSignupView(CreateView):
    model = Student
    form_class= StudentSignupForm
    template_name = 'registration/signup_form_student.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('student_list')

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'students/students_list.html'

    def get_queryset(self):
        return Student.objects.all()


class StudentDetail(DetailView):
    model = Usuario
    context_object_name = 'student_detail'
    template_name = 'students/student_detail.html'



class StudentUpdate(UpdateView):
    model = Usuario
    form_class = StudentUpdateForm
    context_object_name = 'student_update'
    template_name = 'students/student_update.html'
    success_url = reverse_lazy('student_list')

