# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import requests
from config import USERNAME, REPO_OWNER, REPO_NAME

def make_github_issue(title, body=None, assignee=USERNAME, closed=False, labels=[], TOKEN="TOKEN_needed"):
    # Create an issue on github.com using the given parameters
    # Url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/import/issues' % (REPO_OWNER, REPO_NAME)

    # Headers
    headers = {
        "Authorization": "token %s" % TOKEN,
        "Accept": "application/vnd.github.golden-comet-preview+json"
    }

    # Create our issue
    data = {'issue': {'title': title,
                      'body': body,
                      'assignee': assignee,
                      'closed': closed,
                      'labels': labels}}

    payload = json.dumps(data)

    # Add the issue to our repository
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code == 202:
        print ('Successfully created Issue "%s"' % title)
        print(response.status_code)
    else:
        print ('Could not create Issue "%s"' % title)
        print ('Response:', response.content)
        print(response.status_code)


if __name__ == '__main__':
    title = 'Pretty title'
    body = 'Beautiful body'
    assignee = USERNAME
    closed = False
    labels = [
        "imagenet", "image retrieval"
    ]

    make_github_issue(title, body, assignee, closed, labels)
