#!/usr/bin/env python

import requests
import time
import subprocess
import os

username = 'ludflu'
github_repos = f'https://api.github.com/users/{username}/repos'
response = requests.get(url=github_repos)
repos = response.json()

gitlab_token = 'XXXXXXXXXXXXXX'

gitlab_create_repo = f'https://gitlab.com/api/v4/projects?private_token={gitlab_token}'

pwd = os.getcwd()


for repo in repos:
    github_ssh_url = repo['ssh_url']
    repo_name = repo['name']
    req = {'name': repo_name}
    response = requests.post(url=gitlab_create_repo, json=req)
    if response.status_code != 201:
        print(f'error creating gitlab repo {repo_name}. Status: {response.status_code}')
    else:
        print(f'created new repo on gitlab: {repo_name}')
    gitlab_ssh_url = f'git@gitlab.com:{username}/{repo_name}.git'
    subprocess.run(['git', 'clone', github_ssh_url])
    os.chdir(f'{pwd}/{repo_name}')
    subprocess.run(['git', 'remote', 'add', 'gitlab', gitlab_ssh_url])
    subprocess.run(['git', 'push', '-u', 'gitlab', '--all'])
    os.chdir(f'{pwd}')
    time.sleep(10)
