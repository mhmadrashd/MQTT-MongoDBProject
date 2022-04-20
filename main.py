import Components.student as student
import Components.instructor as instructor
import pprint

pp = pprint.PrettyPrinter(indent=2, width=41, compact=True, sort_dicts=False)

# instructor.insertInstructor("Aya", 28, "IOT", True)
# student.insertstudent("Mina", 25, "IOT", ["Java", "C", "Python"])

print("===========Instructors Data===========")
pp.pprint(instructor.getAllInstructors())
print("============================================")

print("===========Students Data===========")
pp.pprint(student.getAllStudents())
print("============================================")
