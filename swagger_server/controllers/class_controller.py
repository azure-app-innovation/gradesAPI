import connexion
import six

from swagger_server.models.assignment import Assignment  # noqa: E501
from swagger_server.models.model_class import ModelClass  # noqa: E501
from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util


def list_assignments(buid, class_id):  # noqa: E501
    """Lists assignments for the class

    Lists assignments for the class # noqa: E501

    :param buid: The caller&#x27;s BUID
    :type buid: str
    :param class_id: List assignments for the class with this classID
    :type class_id: int

    :rtype: List[Assignment]
    """
    return 'do some magic!'


def list_classes(buid, semister):  # noqa: E501
    """Returns a list of classes offered by semister

    Returns a listing of classes offered by semister # noqa: E501

    :param buid: The caller&#x27;s BUID
    :type buid: str
    :param semister: Filter the class list by this semister
    :type semister: str

    :rtype: List[ModelClass]
    """
    return 'do some magic!'


def list_students(buid, class_id):  # noqa: E501
    """Returns a list of students enrolled in the class

    Returns a list of students enrolled in the class # noqa: E501

    :param buid: The caller&#x27;s BUID
    :type buid: str
    :param class_id: Filter the student list by this classID
    :type class_id: str

    :rtype: List[Student]
    """
    return 'do some magic!'
