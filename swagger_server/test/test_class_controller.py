# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.assignment import Assignment  # noqa: E501
from swagger_server.models.model_class import ModelClass  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClassController(BaseTestCase):
    """ClassController integration test stubs"""

    def test_list_assignments(self):
        """Test case for list_assignments

        Lists assignments for the class
        """
        response = self.client.open(
            '/api/v3/class/{classId}/ListAssignments'.format(class_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_classes(self):
        """Test case for list_classes

        Returns a list of classes offered by semister
        """
        query_string = [('semister', 'fall')]
        response = self.client.open(
            '/api/v3/class/listBySemister',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_students(self):
        """Test case for list_students

        Returns a list of students enrolled in the class
        """
        response = self.client.open(
            '/api/v3/class/{classId}/listStudents'.format(class_id='class_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
