# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from apipackage.test import BaseTestCase


class TestInfoController(BaseTestCase):
    """InfoController integration test stubs"""

    def test_get_info(self):
        """Test case for get_info

        info endpoint
        """
        headers = { 
        }
        response = self.client.open(
            '/eve/api/v1/info',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
