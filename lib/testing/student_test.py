from lib.student import Student

def test_student_initialization():
    student = Student("Alice", "Johnson")
    assert student.first_name == "Alice"
    assert student.last_name == "Johnson"

def test_student_learn():
    student = Student("Alice", "Johnson")
    student.learn("Python is fun")
    assert "Python is fun" in student.knowledge
