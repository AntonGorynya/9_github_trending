import requests
from datetime import date, timedelta


def get_trending_repositories(top_size):
    week_ago = date.today() - timedelta(weeks=1)
    url = "https://api.github.com/search/repositories"
    payload = {'q': "created:>{}".format(week_ago), "sort": "stars"}
    top_repo = requests.get(url, params=payload).json()['items'][:top_size]
    return top_repo


def get_open_issues_amount(repo_owner, repo_name):
    url = "https://api.github.com/search/issues"
    payload = {'q': "user:{}".format(repo_owner['login']), 'repo': repo_name}
    responce = requests.get(url, params=payload)
    amount = len([issue for issue in responce.json()['items']
                  if issue['state'] == 'open'])
    return amount


if __name__ == '__main__':
    top_size = 20
    for repo in get_trending_repositories(top_size):
        repo_owner = repo['owner']
        repo_name = repo['name']
        print('repository: {}. Created by {}'
              .format(repo_name, repo_owner['login']))
        print('open issues amount: {}'
              .format(get_open_issues_amount(repo_owner, repo_name)))
