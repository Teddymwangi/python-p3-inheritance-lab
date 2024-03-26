from lib.teacher import Teacher

def test_teacher_initialization():
    teacher = Teacher("Jane", "Smith")
    assert teacher.first_name == "Jane"
    assert teacher.last_name == "Smith"

def test_teacher_teach():
    teacher = Teacher("Jane", "Smith")
    assert teacher.teach() in teacher.knowledge
