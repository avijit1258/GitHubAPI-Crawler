# GitHubAPI-Crawler
This is a fork of @user2589/ghd

## To execute the script
Create token.txt file, and list your GitHub Token per line

## How to create GitHub Tokens
Once you log into your GitHub account, click on your avatar - Settings - Developer settings - Personal access tokens - Generate new token - Generate token (green button at the bottom of the screen). Important: DO NOT CHECK ANY OF THE BOXES THAT DEFINE SCOPES

You could have multiple email accounts (--> multiple GitHub accounts) --> make a token for each. 

## How to contribute
Create a fork, make changes in your fork, and once finish the implementation, submit a PR.

## Scale in fork

main.py
1. A file containing repo names are taken as input. For example,

    ```
    caskroom/homebrew-cask
    kubernetes/kubernetes
    mozilla-b2g/gaia
    ```

2. All the issues of a repo is retrieved.
3. issue_pr_timeline for all the issues retrieved in step-2 are considered to find cross-reference pull request from same organization
4. All the candidate cross-reference pull request events are printed in a text file.

text_to_csv_converter.py
1. Name of the text file generated from previous step is used as command line argument, which is then converted to a well-formatted csv file. 



