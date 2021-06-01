# Class about links inside CountryVaccinationDataRequest _links object
class LinksUrl(object):
    def __init__(self, _self, git, html):
        self._self = _self
        self.git = git
        self.html = html

    def __str__(self):
        return f"self: {self._self}\n" \
               f"git: {self.git}\n" \
               f"html: {self.html}\n"


# Class data about all vaccination in countries
class CountryVaccinationDataRequest(object):
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

    def __str__(self):
        return f"name: {self.name}\n" \
               f"path: {self.path}\n" \
               f"sha: {self.sha}\n" \
               f"size: {self.size}\n" \
               f"url: {self.url}\n" \
               f"html_url: {self.html_url}\n" \
               f"git_url: {self.git_url}\n" \
               f"download_url: {self.download_url}\n" \
               f"type: {self.type}\n" \
               f"_links: {self._links}\n"
