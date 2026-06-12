def show_student(name, course, /, city):
    print(name, course, city)


show_student("Ali", "Python", "Riyadh")
show_student("Sara", "Java", city="Jeddah")


def show_course(student_name, *, course, city):
    print(student_name, course, city)


show_course("Ali", course="Python", city="Riyadh")
show_course("Sara", course="Java", city="Jeddah")
