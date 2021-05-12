from rest_framework import routers
from apps.users.views import UserViewSet
from apps.commits.views import RepositoryViewSet

# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

# Users API
api.register(r'users', UserViewSet)
api.register(r'repos', RepositoryViewSet)
