from rest_framework import viewsets
from apps.commits.models import Repository
from apps.commits.serializers import RepositorySerializer, RepositoryWriteSerializer


class RepositoryViewSet(viewsets.ModelViewSet):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return RepositorySerializer
        return RepositoryWriteSerializer
