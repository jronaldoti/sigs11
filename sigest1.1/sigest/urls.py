"""sigest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from usuarios.views import classroom, student,advisor,supervisor
from usuarios import urls as usuarios_urls
import django.contrib.auth.urls

urlpatterns = [
    path('admin/', admin.site.urls),

    #ACcoounts URLS


    path('accounts/',include(django.contrib.auth.urls)),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', student.StudentSignupView.as_view(), name='student_signup'),
    path('accounts/signup/advisor/', advisor.AdvisorSignupView.as_view(), name='advisor_signup'),
    path('accounts/signup/supervisor/', supervisor.SupervisorSignupView.as_view(), name='supervisor_signup'),


    #Students ULRS

    path('accounts/list/student/', student.StudentListView.as_view(), name='student_list'),
    path('accounts/detail/users/<int:pk>/',student.StudentDetail.as_view(),name='student_detail'),
    path('accounts/update/users/<int:pk>/',student.StudentUpdate.as_view(),name='student_update'),

    #Advisors URLS

    path('accounts/list/advisor/', advisor.AdvisorListView.as_view(), name='advisor_list'),
    path('accounts/detail/<int:pk>/users/',advisor.AdvisorDetail.as_view(),name='advisor_detail'),
    path('accounts/update<int:pk>/users/',advisor.AdvisorUpdate.as_view(),name='advisor_update'),



    # Supervisor URLS
    path('accounts/list/supervisor/', supervisor.SupervisorListView.as_view(), name='supervisor_list'),
    path('accounts/detail/users/<int:pk>/',supervisor.SupervisorDetail.as_view(),name='supervisor_detail'),
    path('accounts/update/users/<int:pk>/',supervisor.SupervisorUpdate.as_view(),name='supervisor_update'),
]
