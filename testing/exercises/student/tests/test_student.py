from unittest import TestCase, main

from exams.exam_10_december_2022.project import Student


class TestStudent(TestCase):

    def setUp(self) -> None:
        self.student = Student("Andrey", {"Java": ["JS"]})

    def test_init(self):
        self.assertEqual("Andrey", self.student.name)
        self.note = {"Java": ["JS"]}
        self.assertEqual(self.note, self.student.courses)

    def test_enroll_if_course_name_is_in_courses(self):
        result = self.student.enroll("Java", ["HTML", "CSS"])
        expected_result = "Course already added. Notes have been updated."

        new_notes = ["JS", "HTML", "CSS"]
        self.assertEqual(new_notes, self.student.courses["Java"])
        self.assertEqual(result, expected_result)

    def test_enroll_if_add_course_notes_is_empty_string(self):
        result = self.student.enroll("C++", ["C"])
        expected_result = "Course and course notes have been added."

        self.assertEqual(["C"], self.student.courses["C++"])
        self.assertEqual(result, expected_result)

    def test_enroll_if_add_course_notes_y(self):
        result = self.student.enroll("C++", ["C"], "Y")
        expected_result = "Course and course notes have been added."

        self.assertEqual(["C"], self.student.courses["C++"])
        self.assertEqual(result, expected_result)


    def test_enroll_if_course_has_been_added(self):
        result = self.student.enroll("Python", ["Django"], "N")
        expected_result = "Course has been added."

        self.assertEqual([], self.student.courses["Python"])
        self.assertEqual(result, expected_result)

    def test_add_notes_if_course_name_is_existing(self):
        result = self.student.add_notes("Java", "Spring")
        expected_result = "Notes have been updated"
        update_notes = ['JS', 'Spring']

        self.assertEqual(update_notes, self.student.courses["Java"])
        self.assertEqual(result, expected_result)

    def test_add_notes_if_course_name_is_not_existing(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("C#", "Nothing")

        expected_message = "Cannot add notes. Course not found."
        self.assertEqual(expected_message, str(ex.exception))

    def test_leave_course_if_course_name_is_existing(self):
        result = self.student.leave_course("Java")
        expected_result = "Course has been removed"

        self.assertEqual({}, self.student.courses)
        self.assertEqual(result, expected_result)

    def test_leave_course_if_course_name_is_not_existing(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("GO")

        expected_message = "Cannot remove course. Course not found."
        self.assertEqual(expected_message, str(ex.exception))


if __name__ == "__main__":
    main()
