def student_info(name, course="Python", city="Riyadh"):
    print(name, course, city)


student_info("Ali")
student_info("Sara", city="Jeddah")
student_info(course="HTML", name="Omar")


def student_info(name, course, /):
    print(name, course)


student_info("Ali", "Python")


def student_info(name, course, /, city):
    print(name, course, city)


student_info(name="Ali", course="Python", city="Riyadh")
