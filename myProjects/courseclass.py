class Course:

    def __init__(self, stu_id):
        self.stu_id = int(stu_id)
        self.course_list = []

    def add_Course(self, course_id):
        self.course_list.append(course_id)

    def edit_Course(self, course_id, new_course_id):
        if course_id in self.course_list:
            self.course_list.pop(course_id)
            self.course_list.append(new_course_id)

    def del_Course(self, course_id):
        if course_id in self.course_list:
            self.course_list.remove(course_id)

    def search_Course(self, course_id, course_type, description, name, year):
        Course.self.course_list = [course_id, course_type, description, name, year]
        while True:
            if course_id in self.course_list:
                return f"{name} ,register in the {year}, {course_type},{self.stu_id}, in department of {description} "

            else:
                return 'Course can not be found'
