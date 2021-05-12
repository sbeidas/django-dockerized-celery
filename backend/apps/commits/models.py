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

    def __str__(self):
        return self.name


class Commit(models.Model):
    repo = models.ForeignKey('commits.Repository', related_name='commits', on_delete=models.CASCADE)
    sha = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    date = models.DateTimeField()
    message = models.TextField()

    def __str__(self):
        return self.sha
