# coding=gbk
# -*- coding:uft-8 -*-
# githubIssue

import requests
import json
import os
from time import sleep
import pandas as pd


def get_closed_issues():
    res_ls = []
    base_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues'
    params = {
        'state': 'closed',
        'per_page': 20
    }
    headers = {'Authorization': f'token {personal_token}'}
    page = 1
    while True:
        params['page'] = page
        print(f'Page: {page}')
        response = requests.get(url=base_url, params=params, headers=headers)
        sleep(1)
        if response.status_code == 200:
            closed_issues = json.loads(response.text)
            if not closed_issues:
                break
            for issue in closed_issues:
                dic = {
                    'title': issue['title'],
                    'html_url': issue['html_url'],
                    'closed_at': issue['closed_at']
                }
                print(dic)
                res_ls.append(dic)
            page += 1
        else:
            print(f'Error: {response.status_code}')
            break
    df = pd.DataFrame(res_ls)
    df.to_excel('data.xlsx', index=False, engine='xlsxwriter')


if __name__ == '__main__':
    os.environ['NO_PROXY'] = 'api.github.com'
    repo_owner = 'repo_owner_name'
    repo_name = 'repo_name'
    personal_token = 'your_token'
    get_closed_issues()
