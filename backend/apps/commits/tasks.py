import requests

from apps.commits.models import Repository, Commit
from config.celery import app


@app.task(bind=True)
def fetch_commits(self, repo_id):
    repo = Repository.objects.get(pk=repo_id)
    repo.status = 'syncing'
    repo.save()

    url = f'https://api.github.com/repos/{repo.name}/commits'
    response = requests.get(url)
    print(response)
    for item in response.json():
        commit = Commit(
            repo=repo,
            sha=item['sha'],
            author=item['commit']['author']['name'],
            date=item['commit']['author']['date'],
            message=item['commit']['message'],
        )
        commit.save()

    repo.status = 'up-to-date'
    repo.save()
