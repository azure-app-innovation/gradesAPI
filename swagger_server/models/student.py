# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Student(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, university_id: str=None, name: str=None, date_enrolled: datetime=None, status: str=None):  # noqa: E501
        """Student - a model defined in Swagger

        :param university_id: The university_id of this Student.  # noqa: E501
        :type university_id: str
        :param name: The name of this Student.  # noqa: E501
        :type name: str
        :param date_enrolled: The date_enrolled of this Student.  # noqa: E501
        :type date_enrolled: datetime
        :param status: The status of this Student.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {
            'university_id': str,
            'name': str,
            'date_enrolled': datetime,
            'status': str
        }

        self.attribute_map = {
            'university_id': 'universityId',
            'name': 'name',
            'date_enrolled': 'dateEnrolled',
            'status': 'status'
        }
        self._university_id = university_id
        self._name = name
        self._date_enrolled = date_enrolled
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'Student':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Student of this Student.  # noqa: E501
        :rtype: Student
        """
        return util.deserialize_model(dikt, cls)

    @property
    def university_id(self) -> str:
        """Gets the university_id of this Student.


        :return: The university_id of this Student.
        :rtype: str
        """
        return self._university_id

    @university_id.setter
    def university_id(self, university_id: str):
        """Sets the university_id of this Student.


        :param university_id: The university_id of this Student.
        :type university_id: str
        """
        if university_id is None:
            raise ValueError("Invalid value for `university_id`, must not be `None`")  # noqa: E501

        self._university_id = university_id

    @property
    def name(self) -> str:
        """Gets the name of this Student.


        :return: The name of this Student.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Student.


        :param name: The name of this Student.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def date_enrolled(self) -> datetime:
        """Gets the date_enrolled of this Student.


        :return: The date_enrolled of this Student.
        :rtype: datetime
        """
        return self._date_enrolled

    @date_enrolled.setter
    def date_enrolled(self, date_enrolled: datetime):
        """Sets the date_enrolled of this Student.


        :param date_enrolled: The date_enrolled of this Student.
        :type date_enrolled: datetime
        """

        self._date_enrolled = date_enrolled

    @property
    def status(self) -> str:
        """Gets the status of this Student.

        Current Status at the university  # noqa: E501

        :return: The status of this Student.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this Student.

        Current Status at the university  # noqa: E501

        :param status: The status of this Student.
        :type status: str
        """
        allowed_values = ["enrolled", "graduated", "unenrolled"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
