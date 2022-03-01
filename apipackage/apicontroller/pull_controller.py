import connexion
import six

from apipackage.models.repo_model import RepoModel  # noqa: E501
from apipackage import util


def get_pull(repo_model=None):  # noqa: E501
    """get configured repos

    gets a list of tracked repos. # noqa: E501

    :param repo_model: 
    :type repo_model: dict | bytes

    :rtype: List[RepoModel]
    """
    if connexion.request.is_json:
        repo_model = RepoModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_pull(repo_model=None):  # noqa: E501
    """post_pull

    Take a repo spec and clone it. # noqa: E501

    :param repo_model: 
    :type repo_model: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        repo_model = RepoModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
