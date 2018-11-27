from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DetailView
from ..models import Usuario,Student
from ..forms import StudentSignupForm
from django.db.models import Count

class StudentSignupView(CreateView):
    model = Usuario
    form_class= StudentSignupForm
    template_name = 'registration/signup_form_student.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('students:student_list')

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'students/students_list.html'

    def get_queryset(self):
        return Student.objects.all()


class StudentDetail(DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'students/student_detail.html'


    def student_detail_view(request, primary_key):
        student = get_object_or_404(Student,pk=primary_key)
        return render(request, 'students/student_detail.html', context={'student':student})

