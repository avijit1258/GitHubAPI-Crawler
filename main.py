from github_api import GitHubAPI
from multiprocessing import Pool
import random


repo = 'hello world'


def mine_cross_reference_pr_issues(repo, pr_ids):
    cross_referenced_issue = []
    for id in pr_ids:
        issue_events = api.get_issue_pr_timeline(repo, id)
        for event in issue_events:
            if event['event'] == 'cross-referenced' and repo not in event['source']['issue']['html_url']:
                cross_referenced_issue.append(id)
                print(event['source']['issue']['html_url'])
                

    if len(cross_referenced_issue) == 0:
        print('No cross referenced pr issue found for repo: ', repo)  
    else:          
        print(cross_referenced_issue)

    return 

def mine_cross_reference_pr_issues_parallel(repo, pr_ids):
    pool = Pool()
    result = pool.map(getting_single_issue, pr_ids)
    return 

def getting_single_issue(id):
    type_repo1 = 'ISSUE'
    type_repo2 = 'ISSUE'
    issue_events = api.get_issue_pr_timeline(repo, id)
    for event in issue_events:
        if event['event'] == 'cross-referenced' and repo not in event['source']['issue']['html_url'] and is_from_same_organization(repo, event['source']['issue']['html_url']):
            type_repo1 = 'ISSUE' if 'issues' in repo else 'PR'
            type_repo2 = 'ISSUE' if 'issues' in event['source']['issue']['html_url'] else 'PR'
            print('https://github.com/', repo, '/issues/', id, ' , ', type_repo1 , ' , ' , event['source']['issue']['html_url'], ',', type_repo2, sep='')
    return

def is_from_same_organization(repo1, repo2):

    # print(repo1.split('/'))
    if repo1.split('/')[3] == repo2.split('/')[3]:
        # print('True')
        return True

    return False

def get_source_of_cross_reference(repo, issue_id):
    # 33773 is a cross-reference event
    url = "repos/%s/issues/%s/events" % (repo, issue_id)
    events = api.request(url, paginate=True, state='all')
    for event in events:
        # print('repo: ' + repo + ' issue: ' + str(issue_id) + ' event: ' + event['event'])
        if event['event'] == 'cross-referenced':
            print(event['source'].get('url'))


if __name__ == "__main__":
    api = GitHubAPI()
    # # query github api with URL
    #     # res = api.request("repos/jquery/jquery/pulls/4406/commits")
    #     #

    # query issue/pr timeline
    # events = api.get_issue_pr_timeline("jquery/jquery", 4406)

    # is_from_same_organization('https://github.com/facebook/react/issues/14981', 'https://github.com/facebook/redux-toolkit/issues/331')

    with open('data/repoList_morethan200PR.txt') as f:
        repos = [line.rstrip() for line in f]
    repos = random.sample(repos, 10)
    repos.append('nodejs/node')
    print(repos)
    for r in repos:
        repo = r
        
        res = api.repo_issues(repo)
        # for pr in res:
        #     print(pr)
        pr_ids = [pr['number'] for pr in res]
        # print(pr_ids)
        mine_cross_reference_pr_issues_parallel(repo, pr_ids)
        
    # get_source_of_cross_reference("nodejs/node", 33773)

    #query repo
    # res = api.get_repo("Jupyter%20Notebook","2008-01-01","2009-01-01")
    
 