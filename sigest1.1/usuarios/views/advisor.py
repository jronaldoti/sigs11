from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render
import requests
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView
from ..models import Usuario
from ..forms import AdvisorSignupForm

class AdvisorSignupView(CreateView):
    model = Usuario
    form_class= AdvisorSignupForm
    template_name = 'registration/signup_form_advisor.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'advisor'
        return super().get_context_data(**kwargs)


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('advisors:advisor_list')

