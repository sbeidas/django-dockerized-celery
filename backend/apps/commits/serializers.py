from rest_framework import serializers
from apps.commits.models import Repository, Commit


class RepositorySerializer(serializers.HyperlinkedModelSerializer):
    commits = serializers.HyperlinkedIdentityField(view_name='repository-commits')

    class Meta:
        model = Repository
        fields = ['url', 'name', 'provider', 'status', 'updated', 'commits']


class RepositoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = ['url', 'name', 'provider']


class CommitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commit
        fields = ['sha', 'author', 'date', 'message']
