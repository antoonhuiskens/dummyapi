# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from apipackage.models.base_model_ import Model
from apipackage import util


class RepoModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, repo=None, dest=None, branch=None):  # noqa: E501
        """RepoModel - a model defined in OpenAPI

        :param repo: The repo of this RepoModel.  # noqa: E501
        :type repo: str
        :param dest: The dest of this RepoModel.  # noqa: E501
        :type dest: str
        :param branch: The branch of this RepoModel.  # noqa: E501
        :type branch: str
        """
        self.openapi_types = {
            'repo': str,
            'dest': str,
            'branch': str
        }

        self.attribute_map = {
            'repo': 'repo',
            'dest': 'dest',
            'branch': 'branch'
        }

        self._repo = repo
        self._dest = dest
        self._branch = branch

    @classmethod
    def from_dict(cls, dikt) -> 'RepoModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The repoModel of this RepoModel.  # noqa: E501
        :rtype: RepoModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def repo(self):
        """Gets the repo of this RepoModel.


        :return: The repo of this RepoModel.
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this RepoModel.


        :param repo: The repo of this RepoModel.
        :type repo: str
        """
        if repo is None:
            raise ValueError("Invalid value for `repo`, must not be `None`")  # noqa: E501

        self._repo = repo

    @property
    def dest(self):
        """Gets the dest of this RepoModel.


        :return: The dest of this RepoModel.
        :rtype: str
        """
        return self._dest

    @dest.setter
    def dest(self, dest):
        """Sets the dest of this RepoModel.


        :param dest: The dest of this RepoModel.
        :type dest: str
        """
        if dest is None:
            raise ValueError("Invalid value for `dest`, must not be `None`")  # noqa: E501

        self._dest = dest

    @property
    def branch(self):
        """Gets the branch of this RepoModel.


        :return: The branch of this RepoModel.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this RepoModel.


        :param branch: The branch of this RepoModel.
        :type branch: str
        """
        if branch is None:
            raise ValueError("Invalid value for `branch`, must not be `None`")  # noqa: E501

        self._branch = branch