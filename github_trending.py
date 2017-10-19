import requests
from datetime import date, timedelta


def get_trending_repositories(top_size):
    start_date = date.today() - timedelta(weeks=1)
    url = "https://api.github.com/search/repositories"
    payload = {'q': "created:>{}".format(start_date), "sort": "stars"}
    top_repo = requests.get(url, params=payload).json()['items'][:top_size]
    return top_repo


def get_open_issues_amount(repo_owner, repo_name):
    amount = 0
    url = "https://api.github.com/search/issues"
    payload = {'q': "user:{}".format(repo_owner['login']), 'repo': repo_name}
    issues = requests.get(url, params=payload)
    for issue in issues.json()['items']:
        if issue['state'] == 'open':
            amount += 1
    return amount


if __name__ == '__main__':
    top_size = 5
    for repo in get_trending_repositories(top_size):
        repo_owner = repo['owner']
        repo_name = repo['name']
        print('repository: {}. Created by {}'
              .format(repo_name, repo_owner['login']))
        print('open issues amount: {}'
              .format(get_open_issues_amount(repo_owner, repo_name)))
