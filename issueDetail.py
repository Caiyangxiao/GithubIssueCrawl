# coding=gbk
# -*- coding:uft-8 -*-
# issueDetail

import requests
import json
import pandas as pd
from time import sleep
import os


def get_issue_comments():
    api_url = issue_html_url.replace('https://github.com/', 'https://api.github.com/repos/') + '/comments'
    headers = {'Authorization': f'token {personal_token}'}
    page = 1
    comments = []
    while True:
        params = {
            'page': page,
            'per_page': 20
        }
        response = requests.get(url=api_url, headers=headers, params=params)
        sleep(1.5)
        if response.status_code == 200:
            comment = json.loads(response.text)
            comments += comment
            if len(comment) < 20:
                return comments
        else:
            print(f'Error: {response.status_code}')
            return comments
        page += 1


def save_comments_to_excel(file, comments):
    if comments:
        data = []
        for comment in comments:
            comment_data = {
                'Author': comment['user']['login'],
                'Body': comment['body'],
                'Created At': comment['created_at']
            }
            data.append(comment_data)
        print(data)
        df = pd.DataFrame(data)
        excel_file = f'{file}.xlsx'
        df.to_excel(excel_file, index=False, engine='xlsxwriter')
        print(f'Comments saved to {excel_file}')


if __name__ == '__main__':
    os.environ['NO_PROXY'] = 'api.github.com'
    personal_token = ''
    issues_html_urls = [i for i in pd.read_excel('data.xlsx', engine='openpyxl')['html_url'].to_list() if
                        '/issues/' in i]
    for issue_html_url in issues_html_urls:
        cms = get_issue_comments()
        issue_id = issue_html_url.split('/')[-1]
        save_comments_to_excel('detail/' + issue_id, cms)
