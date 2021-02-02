from API.repositories.repos import Repos
import json as json_parser


class Github:
    def __init__(self, **kwargs):
        self.api_root_url = "https://api.github.com"
        self.repos = Repos(self.api_root_url, **kwargs)


if __name__ == '__main__':
    r = Github(token="8c5c09e7e91ca44a2e16b85d75ef0dfade350564")
    x = r.repos.list_your_repos()
    print(json_parser.dumps(json_parser.loads(x.text), indent=2))
