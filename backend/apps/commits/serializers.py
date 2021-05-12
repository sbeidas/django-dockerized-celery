from rest_framework import serializers
from apps.commits.models import Repository, Commit


class RepositorySerializer(serializers.ModelSerializer):
    commits = serializers.HyperlinkedIdentityField(view_name='repository-commits')

    class Meta:
        model = Repository
        fields = ['name', 'provider', 'status', 'commits']


class RepositoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = ['name', 'provider']


class CommitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commit
        fields = ['sha', 'author', 'date', 'message']
