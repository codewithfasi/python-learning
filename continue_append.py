courses = ["  python  ", "CANCELLED", "   ", "java", " cancelled ", "HTML", "css"]
counter = 0
valid_courses = []
for course in courses:
    clean_course = course.strip().title()
    if clean_course == "":
        print("Empty course skipped")
        continue

    if clean_course == "Cancelled":
        print("Cancelled course skipped")
        continue

    counter = counter + 1
    valid_courses.append(clean_course)
    print("Valid course:", clean_course)
print("Total valid courses:", counter)
print("Valid courses:", valid_courses)
print("Course registration check completed")
