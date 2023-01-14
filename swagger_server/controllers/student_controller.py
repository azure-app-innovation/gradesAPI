import connexion
import six

from swagger_server.models.grade import Grade  # noqa: E501
from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util


def add_student(body, buid):  # noqa: E501
    """Enroll a new student to the university

    Adds a new student to the university # noqa: E501

    :param body: Create a new student in the university
    :type body: dict | bytes
    :param buid: The caller&#x27;s BUID
    :type buid: str

    :rtype: Student
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_student(university_id, name, date_enrolled, status, buid):  # noqa: E501
    """Enroll a new student to the university

    Adds a new student to the university # noqa: E501

    :param university_id: 
    :type university_id: str
    :param name: 
    :type name: str
    :param date_enrolled: 
    :type date_enrolled: str
    :param status: 
    :type status: str
    :param buid: The caller&#x27;s BUID
    :type buid: str

    :rtype: Student
    """
    date_enrolled = util.deserialize_datetime(date_enrolled)
    return 'do some magic!'


def delete_student(student_id, api_key=None):  # noqa: E501
    """Deletes a student

    delete a student # noqa: E501

    :param student_id: Student id to delete
    :type student_id: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def find_students_by_status(buid, status):  # noqa: E501
    """Finds Students by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param buid: The caller&#x27;s BUID
    :type buid: str
    :param status: Status values that need to be considered for filter
    :type status: str

    :rtype: List[Student]
    """
    return 'do some magic!'


def get_student_by_id(student_id):  # noqa: E501
    """Find student by ID

    Returns a single student # noqa: E501

    :param student_id: ID of student to return
    :type student_id: int

    :rtype: Student
    """
    return 'do some magic!'


def list_grades(buid, student_id, class_id):  # noqa: E501
    """Lists student grades in a class

    Lists student grades in a class # noqa: E501

    :param buid: The caller&#x27;s BUID
    :type buid: str
    :param student_id: ID of the student whose grades to return
    :type student_id: str
    :param class_id: 
    :type class_id: str

    :rtype: List[Grade]
    """
    return 'do some magic!'


def update_student(body, buid, student_id):  # noqa: E501
    """Update an existing student

    Update an existing student by Id # noqa: E501

    :param body: Update an existent student enrolled in the university
    :type body: dict | bytes
    :param buid: The caller&#x27;s BUID
    :type buid: str
    :param student_id: ID of student to update
    :type student_id: str

    :rtype: Student
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_student(university_id, name, date_enrolled, status, buid, student_id):  # noqa: E501
    """Update an existing student

    Update an existing student by Id # noqa: E501

    :param university_id: 
    :type university_id: str
    :param name: 
    :type name: str
    :param date_enrolled: 
    :type date_enrolled: str
    :param status: 
    :type status: str
    :param buid: The caller&#x27;s BUID
    :type buid: str
    :param student_id: ID of student to update
    :type student_id: str

    :rtype: Student
    """
    date_enrolled = util.deserialize_datetime(date_enrolled)
    return 'do some magic!'


def update_student_with_form(student_id, name=None, status=None):  # noqa: E501
    """Updates a student in the university with form data

     # noqa: E501

    :param student_id: ID of student that needs to be updated
    :type student_id: int
    :param name: Name of student that needs to be updated
    :type name: str
    :param status: Status of student that needs to be updated
    :type status: str

    :rtype: None
    """
    return 'do some magic!'
