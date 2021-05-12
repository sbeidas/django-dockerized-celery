import requests

from apps.commits.models import Repository, Commit
from config.celery import app


@app.task(bind=True)
def fetch_commits(self, repo_id):
    repo = Repository.objects.get(pk=repo_id)

    # Allow only one sync job per repo
    if repo.status == 'syncing':
        return f'Fetching commits for {repo.name} is already in progress; ignoring request'

    repo.status = 'syncing'
    repo.save()

    url = f'https://api.github.com/repos/{repo.name}/commits'
    processed = 0

    while url:
        response = requests.get(url)

        # This isn't a general error-handling strategy; it's a quick work-around for GitHub
        # rate limiting so the repo isn't stuck forever in the 'syncing' state
        if response.status_code != 200:
            print(f'Error fetching commits for {repo.name}; reason:')
            print(response.text)
            break

        commits = []
        for item in response.json():
            commits.append(Commit(
                repo=repo,
                sha=item['sha'],
                author=item['commit']['author']['name'],
                date=item['commit']['author']['date'],
                message=item['commit']['message'],
            ))
        Commit.objects.bulk_create(commits)
        processed += len(commits)

        if 'next' in response.links:
            url = response.links['next']['url']
        else:
            url = None

    repo.status = 'up-to-date'
    repo.save()

    return f'Fetched {processed} commits'
