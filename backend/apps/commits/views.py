from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.commits.models import Repository, Commit
from apps.commits.serializers import RepositorySerializer, RepositoryWriteSerializer, CommitSerializer


class RepositoryViewSet(viewsets.ModelViewSet):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return RepositorySerializer
        return RepositoryWriteSerializer

    @action(detail=True)
    def commits(self, request, *args, **kwargs):
        repo = self.get_object()
        commits = Commit.objects.filter(repo=repo)
        serializer = CommitSerializer(commits, many=True)
        return Response(serializer.data)


class CommitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Commit.objects.all()
    serializer_class = CommitSerializer
