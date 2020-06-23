# goodbye-github
script to migrate away from github


- [Github does business with and enables ICE](https://techcrunch.com/2019/11/13/github-faces-more-resignations-in-light-of-ice-contract/) (Immigration and Customs Enforcement). 
- ICE is still [jailing innocent children](https://www.washingtonpost.com/opinions/migrant-children-are-still-confined-and-vulnerable-its-a-gratuitous-act-of-cruelty/2020/05/25/8884fc4a-9bb5-11ea-a2b3-5c3f2d1586df_story.html)
- Github employees have [resigned in protest](https://techcrunch.com/2019/11/13/github-faces-more-resignations-in-light-of-ice-contract/)
- I don't want to support Github as long as it enables the morally indefensible collaboration with ICE.
- I've used this script to migrate my [personal source code repos](https://gitlab.com/ludflu) to Gitlab


## To use this script

1. Sign up for [Gitlab](https://gitlab.com/) 
2. Go get a [Gitlab personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) and [configure the script](https://github.com/ludflu/goodbye-github/blob/main/migrate.py#L13) with it.
3. Make sure your ssh pubkey is [configured for access to both Github](https://devconnected.com/how-to-setup-ssh-keys-on-github/) and for [access to Gitlab](https://docs.gitlab.com/ee/ssh/#adding-an-ssh-key-to-your-gitlab-account).
4. Install the `requests` library using `pip install requests`
5. Run the script from the command line `./migrate.py`
6. Manually delete all your github repos.
