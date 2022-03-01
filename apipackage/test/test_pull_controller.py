# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from apipackage.models.repo_model import RepoModel  # noqa: E501
from apipackage.test import BaseTestCase


class TestPullController(BaseTestCase):
    """PullController integration test stubs"""

    def test_get_pull(self):
        """Test case for get_pull

        get configured repos
        """
        repo_model = {"repo":"string","dest":"string","branch":"string"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/eve/api/v1/pull',
            method='GET',
            headers=headers,
            data=json.dumps(repo_model),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_pull(self):
        """Test case for post_pull

        
        """
        repo_model = {"repo":"string","dest":"string","branch":"string"}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/eve/api/v1/pull',
            method='POST',
            headers=headers,
            data=json.dumps(repo_model),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
