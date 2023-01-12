# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.grade import Grade  # noqa: E501
from swagger_server.models.student import Student  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStudentController(BaseTestCase):
    """StudentController integration test stubs"""

    def test_add_student(self):
        """Test case for add_student

        Enroll a new student to the university
        """
        body = Student()
        query_string = [('buid', 'buid_example')]
        data = dict(university_id='university_id_example',
                    name='name_example',
                    semester_enrolled='2013-10-20T19:20:30+01:00',
                    status='status_example')
        response = self.client.open(
            '/api/v3/student',
            method='POST',
            data=json.dumps(body),
            data=data,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_student(self):
        """Test case for delete_student

        Deletes a student
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/api/v3/student/{studentId}'.format(student_id=789),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_students_by_status(self):
        """Test case for find_students_by_status

        Finds Students by status
        """
        query_string = [('buid', 'buid_example'),
                        ('status', 'enrolled')]
        response = self.client.open(
            '/api/v3/student/findByStatus',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_student_by_id(self):
        """Test case for get_student_by_id

        Find student by ID
        """
        response = self.client.open(
            '/api/v3/student/{studentId}'.format(student_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_grades(self):
        """Test case for list_grades

        Lists student grades in a class
        """
        query_string = [('buid', 'buid_example')]
        response = self.client.open(
            '/api/v3/student/{studentId}/{classId}/listGrades'.format(student_id='student_id_example', class_id='class_id_example'),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_student(self):
        """Test case for update_student

        Update an existing student
        """
        body = Student()
        query_string = [('buid', 'buid_example')]
        data = dict(university_id='university_id_example',
                    name='name_example',
                    semester_enrolled='2013-10-20T19:20:30+01:00',
                    status='status_example')
        response = self.client.open(
            '/api/v3/student/{studentId}'.format(student_id='student_id_example'),
            method='PUT',
            data=json.dumps(body),
            data=data,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_student_with_form(self):
        """Test case for update_student_with_form

        Updates a student in the university with form data
        """
        query_string = [('name', 'name_example'),
                        ('status', 'status_example')]
        response = self.client.open(
            '/api/v3/student/{studentId}'.format(student_id=789),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
