from django.db import models

PROVIDERS = [
    ('github', 'GitHub'),
    ('bitbucket', 'BitBucket'),
]

STATUSES = [
    ('up-to-date', 'Up-To-Date'),
    ('syncing', 'Syncing')
]


class Repository(models.Model):
    name = models.CharField(max_length=100)
    provider = models.CharField(max_length=20, choices=PROVIDERS)
    status = models.CharField(max_length=20, choices=STATUSES)
