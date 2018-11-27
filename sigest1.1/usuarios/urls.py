from django.urls import path

from .views import student,advisor

app_name = 'usuarios'

urlpatterns = [
    path('list/', student.StudentListView.as_view(), name='student_list'),
]