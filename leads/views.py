from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import *
# Create your views here.

class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = 'leads/lead_list.html'
    # queryset = Lead.objects.all()
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user
        #initial queryset of leads for the oraganization
        if user.is_organizor:
            queryset = Lead.objects.filter(
                organization = user.userprofile,
                agent__isnull=False
                )
        else:
            queryset = Lead.objects.filter(
                organization = user.agent.organization,
                agent__isnull=False
                )
            #filter for the agent that is logged in
            queryset = queryset.filter(agent__user= self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(LeadListView, self).get_context_data(**kwargs)

        if user.is_organizor:
            queryset = Lead.objects.filter(
                organization = user.userprofile,
                agent__isnull = True,
            )

            context.update({
                "unassigned_Leads": queryset,
            })

        return context

# def lead_list(request):
#     leads = Lead.objects.all()
#     context={
#         'leads':leads,
#     }

#     return render(request, 'leads/lead_list.html', context)

class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'leads/lead_detail.html'
    # queryset = Lead.objects.all()
    context_object_name = 'lead'

    def get_queryset(self):
        user = self.request.user
        #initial queryset of leads for the oraganization
        if user.is_organizor:
            queryset = Lead.objects.filter(organization = user.userprofile)
        else:
            queryset = Lead.objects.filter(organization = user.agent.organization)
            #filter for the agent that is logged in
            queryset = queryset.filter(agent__user= self.request.user)
        return queryset

# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)

#     return render(request, 'leads/lead_detail.html', {'lead':lead})

class LeadCreateView(OrganizorAndLoginRequiredMixin, generic.CreateView):
    model = Lead
    template_name = 'leads/add_lead.html'
    form_class = AddLeadForm

    def get_success_url(self):
        return reverse("lead_list")

# def add_lead(request):
#     form = AddLeadForm()
#     if request.method == "POST":
#         form = AddLeadForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('lead_list')
        
#     else:
#         print("Form is not valid")
#         print(form.errors)
#         print(request.POST)
#         form = AddLeadForm()
#     context= {
#         'form': form
#     }
#     return render(request, 'leads/add_lead.html', context)

class LeadUpdateView(OrganizorAndLoginRequiredMixin, generic.UpdateView):
    model = Lead
    template_name = 'leads/edit_lead.html'
    form_class = AddLeadForm

    def get_success_url(self):
        return reverse("lead_list")
    
    def get_queryset(self):
        user = self.request.user
        #initial queryset of leads for the oraganization
        # if user.is_organizor:
        #     queryset = Lead.objects.filter(organization = user.userprofile)
        # else:
        #     queryset = Lead.objects.filter(organization = user.agent.organization)
        #     #filter for the agent that is logged in
        #     queryset = queryset.filter(agent__user= self.request.user)
        return Lead.objects.filter(organization = user.userprofile)



# def edit_lead(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = AddLeadForm(instance=lead)

#     if request.method == "POST":
#         form = AddLeadForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('lead_detail', kwargs={'pk': lead.pk}))
#     context={
#         'form':form,
#         'lead':lead,
#     }

#     return render(request, 'leads/edit_lead.html', context)

class LeadDeleteView(OrganizorAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'leads/delete_lead.html'
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return reverse('lead_list')
    
    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organization = user.userprofile)


# def delete_lead(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect('lead_list')

class LandingPageView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'landing_page.html'


# def landing_page(request):
#     return render(request, 'landing_page.html')

class AssignAgentView(OrganizorAndLoginRequiredMixin, generic.FormView):
    template_name = 'leads/assign_agent.html'
    form_class = AssignAgentForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs 

    def get_success_url(self):
        return reverse('lead_list')
    
    def form_valid(self, form):
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView,self).form_valid(form)