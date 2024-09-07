from django.urls import path
from .views import *

urlpatterns=[
    path('', LeadListView.as_view(), name='lead_list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
    path('create_lead/',LeadCreateView.as_view(), name='add_lead'),
    path('<int:pk>/edit/', LeadUpdateView.as_view() , name='edit_lead'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='delete_lead'),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name='Assign-Agent'),
]