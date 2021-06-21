import requests
import environ
import json
from api.requests import GithubDataRepoRequest
from humps import decamelize

env = environ.Env()


def get_content_data_repo(env_name: str):
    response = requests.get(env(env_name))
    list_data = decamelize(json.loads(response.content))
    return [GithubDataRepoRequest(**x) for x in list_data]
