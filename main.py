from github_api import GitHubAPI


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

def get_source_of_cross_reference(repo, issue_id):
    # 33773 is a cross-reference event
    url = "repos/%s/issues/%s/events" % (repo, issue_id)
    events = api.request(url, paginate=True, state='all')
    for event in events:
        # print('repo: ' + repo + ' issue: ' + str(issue_id) + ' event: ' + event['event'])
        if event['event'] == 'cross-referenced':
            print(event['source'].get('url'))

    return 


if __name__ == "__main__":
    api = GitHubAPI()
    # # query github api with URL
    #     # res = api.request("repos/jquery/jquery/pulls/4406/commits")
    #     #

    # query issue/pr timeline
    # events = api.get_issue_pr_timeline("jquery/jquery", 4406)
    repo = input("Enter repo: ")
    res = api.repo_issues("nodejs/node")
    # for pr in res:
    #     print(pr)
    pr_ids = [pr['number'] for pr in res]
    # print(pr_ids)
    mine_cross_reference_pr_issues(repo, pr_ids)
    # get_source_of_cross_reference("nodejs/node", 33773)

    #query repo
    # res = api.get_repo("Jupyter%20Notebook","2008-01-01","2009-01-01")
    print()
