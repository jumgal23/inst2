# api/urls.py
from django.urls import path
from .views import PublicationListCreateView, PublicationRetrieveUpdateDestroyView, PublicationLikeCreateDeleteView

app_name = 'api'

urlpatterns = [
    path('publications/', PublicationListCreateView.as_view(), name='publication-list-create'),
    path('publications/<int:pk>/', PublicationRetrieveUpdateDestroyView.as_view(), name='publication-retrieve-update-destroy'),
    path('publications/<int:pk>/like/', PublicationLikeCreateDeleteView.as_view(), name='publication-like-create-delete'),
]
