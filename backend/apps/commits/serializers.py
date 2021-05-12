from rest_framework import serializers
from apps.commits.models import Repository


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = ['name', 'provider', 'status']
