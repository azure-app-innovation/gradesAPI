import connexion
import six

from swagger_server.models.assignment import Assignment  # noqa: E501
from swagger_server.models.model_class import ModelClass  # noqa: E501
from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util


def list_assignments(class_id, buid=None):  # noqa: E501
    """Lists assignments for the class

    Lists assignments for the class # noqa: E501

    :param class_id: List assignments for the class with this classID
    :type class_id: int
    :param buid: The caller&#x27;s BUID
    :type buid: str

    :rtype: List[Assignment]
    """
    return 'do some magic!'


def list_classes(semister, buid=None):  # noqa: E501
    """Returns a list of classes offered by semister

    Returns a listing of classes offered by semister # noqa: E501

    :param semister: Filter the class list by this semister
    :type semister: str
    :param buid: The caller&#x27;s BUID
    :type buid: str

    :rtype: List[ModelClass]
    """
    return 'do some magic!'


def list_students(class_id, buid=None):  # noqa: E501
    """Returns a list of students enrolled in the class

    Returns a list of students enrolled in the class # noqa: E501

    :param class_id: Filter the student list by this classID
    :type class_id: str
    :param buid: The caller&#x27;s BUID
    :type buid: str

    :rtype: List[Student]
    """
    return 'do some magic!'
