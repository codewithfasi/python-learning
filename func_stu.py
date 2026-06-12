def student_result_check(student, score, blocked, completed_course):
    if score >= 50 and not blocked and completed_course:
        print(student, "Passed")
    else:
        print(student, "Failed")


student_result_check("Ali", 75, False, True)
student_result_check("Sara", 45, False, True)
student_result_check("Omar", 80, True, True)
student_result_check("Mona", 90, False, False)
