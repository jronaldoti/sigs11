from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render
import requests
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DetailView
from ..models import Usuario,Advisor
from ..forms import AdvisorSignupForm,AdvisorUpdateForm

class AdvisorSignupView(CreateView):
    model = Advisor
    form_class= AdvisorSignupForm
    template_name = 'registration/signup_form_advisor.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'advisor'
        return super().get_context_data(**kwargs)


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('advisor_list')

class AdvisorListView(ListView):
    model = Advisor
    context_object_name = 'advisors'
    template_name = 'advisors/advisors_list.html'

class AdvisorDetail(DetailView):
    model = Usuario
    context_object_name = 'advisor_detail'
    template_name = 'advisors/advisor_detail.html'

class AdvisorUpdate(UpdateView):
    model = Usuario
    form_class = AdvisorUpdateForm
    context_object_name = 'advisor_update'
    template_name = 'advisors/advisor_update.html'
    success_url = reverse_lazy('advisor_list')
