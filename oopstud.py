class Student:
    def __init__(self, student_id: str, name: str, marks: float):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Marks: {self.marks}"


class StudentRecords:
    def __init__(self):
        self._students: dict[str, Student] = {}

    def add_student(self, student: Student):
        if student.student_id in self._students:
            print(f"Student with ID {student.student_id} already exists.")
        else:
            self._students[student.student_id] = student
            print("Student added successfully.")

    def print_all(self):
        if not self._students:
            print("No student records.")
        else:
            print("\nAll students:")
            for s in self._students.values():
                print(s)
            print()

    def find_student(self, student_id: str):
        student = self._students.get(student_id)
        if student:
            print("Found:", student)
        else:
            print("Student not found.")

    def delete_student(self, student_id: str):
        if student_id in self._students:
            del self._students[student_id]
            print("Deleted successfully.")
        else:
            print("Student not found.")

    def update_student(self, student_id: str, new_name: str, new_marks: float):
        student = self._students.get(student_id)
        if student:
            student.name = new_name
            student.marks = new_marks
            print("Updated successfully.")
        else:
            print("Student not found.")


def main():
    records = StudentRecords()

    menu = """
    1. Print all students
    2. Find student
    3. Delete student
    4. Update student
    5. Add student
    6. Exit
    """

    while True:
        print(menu)
        choice = input("Enter choice (1–6): ").strip()
        if choice == "1":
            records.print_all()
        elif choice == "2":
            sid = input("Enter student ID to find: ").strip()
            records.find_student(sid)
        elif choice == "3":
            sid = input("Enter student ID to delete: ").strip()
            records.delete_student(sid)
        elif choice == "4":
            sid = input("Enter student ID to update: ").strip()
            if sid:
                name = input("Enter new name: ").strip()
                marks = float(input("Enter new marks: ").strip())
                records.update_student(sid, name, marks)
        elif choice == "5":
            sid = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            marks = float(input("Enter Student Marks: ").strip())
            records.add_student(Student(sid, name, marks))
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1–6.")
        print()

if __name__ == "__main__":
    main()
