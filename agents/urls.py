from django.urls import path
from .views import *
urlpatterns = [
    path('',AgentListView.as_view(), name='agentlist' ),
    path('create/', AgentCreateView.as_view(), name='agentcreate'),
    path('<int:pk>/detail/', AgentDetailView.as_view(), name='agent_detail'),
    path('<int:pk>/edit/', AgentEditView.as_view(), name='edit_agent'),
    path('<int:pk>/delete/', AgentDeleteView.as_view(), name='delete_agent'),
]