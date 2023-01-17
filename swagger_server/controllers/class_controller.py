import connexion
import six

from swagger_server.models.assignment import Assignment  # noqa: E501
from swagger_server.models.model_class import ModelClass  # noqa: E501
from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util


def add_class(body, buid):  # noqa: E501
    """create a new class to the university

    Adds a new class to the university # noqa: E501

    :param body: Create a new class in the university
    :type body: dict | bytes
    :param buid: The caller&#x27;s BUID
    :type buid: str

    :rtype: ModelClass
    """
    if connexion.request.is_json:
        body = ModelClass.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_class(class_id, title, description, meeting_time, meeting_location, status, semester, buid):  # noqa: E501
    """create a new class to the university

    Adds a new class to the university # noqa: E501

    :param class_id: 
    :type class_id: str
    :param title: 
    :type title: str
    :param description: 
    :type description: str
    :param meeting_time: 
    :type meeting_time: str
    :param meeting_location: 
    :type meeting_location: str
    :param status: 
    :type status: str
    :param semester: 
    :type semester: str
    :param buid: The caller&#x27;s BUID
    :type buid: str

    :rtype: ModelClass
    """
    return 'do some magic!'


def get_class_by_id(buid, class_id):  # noqa: E501
    """Find student by ID

    Returns a single student # noqa: E501

    :param buid: The caller&#x27;s BUID
    :type buid: str
    :param class_id: ID of student to return
    :type class_id: str

    :rtype: Student
    """
    return 'do some magic!'


def list_assignments(buid, class_id):  # noqa: E501
    """Lists assignments for the class

    Lists assignments for the class # noqa: E501

    :param buid: The caller&#x27;s BUID
    :type buid: str
    :param class_id: List assignments for the class with this classID
    :type class_id: str

    :rtype: List[Assignment]
    """
    return 'do some magic!'


def list_classes(buid, semester):  # noqa: E501
    """Returns a list of classes offered by semester

    Returns a listing of classes offered by semester # noqa: E501

    :param buid: The caller&#x27;s BUID
    :type buid: str
    :param semester: Filter the class list by this semester
    :type semester: str

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

    :rtype: List[str]
    """
    return 'do some magic!'
