from rest_framework import viewsets
from apps.commits.models import Repository
from apps.commits.serializers import RepositorySerializer


class RepositoryViewSet(viewsets.ModelViewSet):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
