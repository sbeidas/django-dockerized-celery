from django.db import models

PROVIDERS = [
    ('github', 'GitHub'),
    ('bitbucket', 'BitBucket'),
]

STATUSES = [
    ('out-of-date', 'Out-of-Date'),
    ('syncing', 'Syncing'),
    ('up-to-date', 'Up-to-Date'),
]


class Repository(models.Model):
    name = models.CharField(max_length=100, unique=True)
    provider = models.CharField(max_length=20, choices=PROVIDERS)
    status = models.CharField(max_length=20, choices=STATUSES, default='out-of-date')
    updated = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pk']  # I'm just being lazy here


class Commit(models.Model):
    repo = models.ForeignKey('commits.Repository', related_name='commits', on_delete=models.CASCADE)
    sha = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    date = models.DateTimeField()
    message = models.TextField()

    def __str__(self):
        return self.sha

    class Meta:
        ordering = ['date']
