from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import *
from .forms import *
from .mixins import *

# Create your views here.

class AgentListView(OrganizorAndLoginRequiredMixin, generic.ListView):
    template_name = "agents/agentlist.html"

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
    

class AgentCreateView(OrganizorAndLoginRequiredMixin, generic.CreateView):
    template_name= 'agents/agentcreate.html'
    form_class = AddAgentForm

    def get_success_url(self):
        return reverse('agentlist')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organizor = False
        user.save()
        Agent.objects.create(
            user=user,
            organization = self.request.user.userprofile
        )
        # agent.organization = self.request.user.userprofile
        # agent.save()
        return super(AgentCreateView, self).form_valid(form)
    
class AgentDetailView(OrganizorAndLoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agentdetail.html'
    context_object_name = 'agent'

    def get_queryset(self):
        return Agent.objects.all()


class AgentEditView(OrganizorAndLoginRequiredMixin, generic.UpdateView):
    model = Agent
    template_name = 'agents/edit_agent.html'
    form_class = AddAgentForm

    def get_queryset(self):
        return Agent.objects.all()

    def get_success_url(self):
        return reverse('agent_detail')



class AgentDeleteView(OrganizorAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/delete_agent.html'
    context_object_name = "agent"

    def get_queryset(self):
        return Agent.objects.all()
    
    def get_success_url(self):
        return reverse('agentlist')


