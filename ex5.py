import json
import os


def names_of_registered_students(input_json_path, course_name):
    """
    This function returns a list of the names of the students who registered for
    the course with the name "course_name".

    :param input_json_path: Path of the students database json file.
    :param course_name: The name of the course.
    :return: List of the names of the students.
    """
    file = open(input_json_path)
    data = json.load(file)
    students = []
    for line in data.values():
        if course_name in line['registered_courses']:
            students.append(line['student_name'])
    file.close()
    return students


def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    with open(input_json_path) as json_file:
        data = json.load(json_file)
        courses = {}
        for line in data.values():
            for course in line['registered_courses']:
                if course in courses:
                    courses[course] += 1
                else:
                    courses[course] = 1
    sorted_courses = sorted(courses.keys())
    with open(output_file_path , 'w') as file:
        for course in sorted_courses:
            file.write('"{}" {}\n'.format(course, courses[course]))


def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    courses = {}
    for file_name in [file for file in os.listdir(json_directory_path) if file.endswith('.json')]:
        file_path = os.path.join(json_directory_path, file_name)
        with open(file_path) as json_file:
            data = json.load(json_file)
            for line in data.values():
                course_name = line['course_name']
                lecturers = line['lecturers']
                if course_name in courses.keys():
                    for lecturer in lecturers:
                        if lecturer not in courses[course_name]:
                            courses[course_name].append(lecturer)
                else:
                    courses[course_name] = lecturers
    lecturers_dict = {}
    for course_name, lecturers in courses.items():
        for lecturer in lecturers:
            if lecturer not in lecturers_dict.keys():
                lecturers_dict[lecturer] = [course_name]
            else:
                if course_name not in lecturers_dict[lecturer]:
                    lecturers_dict[lecturer].append(course_name)
    with open(output_json_path, 'w') as file:
        file.write(json.dumps(lecturers_dict))



