from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render
import requests
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DetailView
from ..models import Usuario, Supervisor
from ..forms import SupervisorSignupForm,SupervisorUpdateForm

class SupervisorSignupView(CreateView):
    model = Supervisor
    form_class= SupervisorSignupForm
    template_name = 'registration/signup_form_supervisor.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'supervisor'
        return super().get_context_data(**kwargs)


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('supervisor_list')

class SupervisorListView(ListView):
    model = Supervisor
    context_object_name = 'supervisors'
    template_name = 'supervisors/supervisors_list.html'


class SupervisorDetail(DetailView):
    model = Usuario
    context_object_name = 'supervisor_detail'
    template_name = 'supervisors/supervisor_detail.html'


class SupervisorUpdate(UpdateView):
    model = Usuario
    form_class = SupervisorUpdateForm
    context_object_name = 'supervisor_update'
    template_name = 'supervisors/supervisor_update.html'
    success_url = reverse_lazy('supervisor_list')

