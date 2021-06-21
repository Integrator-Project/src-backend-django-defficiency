from utils import auto_str


@auto_str
class LinksUrl:
    def __init__(self, _self, git, html):
        self._self = _self
        self.git = git
        self.html = html


@auto_str
class GithubDataRepoRequest:
    def __init__(self, name, path, sha, size,
                 url, html_url, git_url,
                 download_url, type, _links):
        self.name = name
        self.path = path
        self.sha = sha
        self.size = size
        self.url = url
        self.html_url = html_url
        self.git_url = git_url
        self.download_url = download_url
        self.type = type
        self._links = _links
