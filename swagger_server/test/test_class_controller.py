# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.assignment import Assignment  # noqa: E501
from swagger_server.models.model_class import ModelClass  # noqa: E501
from swagger_server.models.student import Student  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClassController(BaseTestCase):
    """ClassController integration test stubs"""

    def test_add_class(self):
        """Test case for add_class

        create a new class to the university
        """
        body = ModelClass()
        query_string = [('buid', 'buid_example')]
        data = dict(class_id='class_id_example',
                    title='title_example',
                    description='description_example',
                    meeting_time='meeting_time_example',
                    meeting_location='meeting_location_example',
                    status='status_example',
                    semester='semester_example')
        response = self.client.open(
            '/api/class',
            method='POST',
            data=json.dumps(body),
            data=data,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_assignments(self):
        """Test case for list_assignments

        Lists assignments for the class
        """
        query_string = [('buid', 'buid_example')]
        response = self.client.open(
            '/api/class/ListAssignments/{classId}'.format(class_id=789),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_classes(self):
        """Test case for list_classes

        Returns a list of classes offered by semester
        """
        query_string = [('buid', 'buid_example')]
        response = self.client.open(
            '/api/class/listBySemester/{semester}'.format(semester='semester_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_students(self):
        """Test case for list_students

        Returns a list of students enrolled in the class
        """
        query_string = [('buid', 'buid_example')]
        response = self.client.open(
            '/api/class/listStudents/{classId}'.format(class_id='class_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
