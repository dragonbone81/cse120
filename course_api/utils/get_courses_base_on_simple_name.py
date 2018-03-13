from course_api.models import Course
from course_api.serializers import CourseSerializer


def get_courses(courses_to_search):
    courses = dict()
    for course in courses_to_search:
        courses[course] = [CourseSerializer(course).data for course in
                           Course.objects.filter(simple_name__iexact=course)]
    return courses
