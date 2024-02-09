# api/views.py
from rest_framework import generics, permissions
from webapp.models import Publication
from .serializers import PublicationSerializer

class PublicationListCreateView(generics.ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can view

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PublicationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can edit/delete

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()

class PublicationLikeCreateDeleteView(generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can like/unlike

    def perform_create(self, serializer):
        publication_id = self.kwargs['pk']
        publication = Publication.objects.get(pk=publication_id)
        publication.users_like.add(self.request.user)

    def perform_destroy(self, serializer):
        publication_id = self.kwargs['pk']
        publication = Publication.objects.get(pk=publication_id)
        publication.users_like.remove(self.request.user)
