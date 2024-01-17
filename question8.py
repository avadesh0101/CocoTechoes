# This playground contains the Python version of the code from the blog post
# https://hurryabit.github.io/blog/stack-safety-for-free/
import random

class Student:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects

    def get_total_marks(self):
        return sum(subject[1] for subject in self.subjects.values())

def generate_random_data():
    students = []

    for i in range(1, 21):
        name = f"Student{i}"
        subjects = {}

        for j in range(1, 6):
            subject_name = f"Subject{j}"
            total_marks = 100  # Assuming total marks for each subject is 100
            marks_scored = random.randint(0, total_marks)

            subjects[subject_name] = (total_marks, marks_scored)

        students.append(Student(name, subjects))

    return students

def main():
    students = generate_random_data()

    # Sort students based on total marks in descending order
    students.sort(key=lambda student: student.get_total_marks(), reverse=True)

    # Display top five students
    print("Top Five Students:")
    for student in students[:5]:
        print(f"{student.name} - Total Marks: {student.get_total_marks()}")

if __name__ == "__main__":
    main()