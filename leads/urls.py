from django.urls import path
from .views import (
                  LeadListView,
                  LeadDetailView,
                  LeadCreateView,
                  LeadUpdateView,
                  LeadDeleteView,
                  AssignAgentView,
                  CategoryListView,
CategoryDetailView,
LeadCategoryUpdateView,
                    )

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name='lead_list'),
    path('<int:pk>/detail/', LeadDetailView.as_view(), name='lead_detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead_update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead_delete'),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name='assign-agent'),
    path('<int:pk>/category/', LeadCategoryUpdateView.as_view(), name='lead-category-update'),
    path('create/', LeadCreateView.as_view(), name='lead_create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
        path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]