employees = [
    {"name": "  ahmed ", "status": "Present", "hours": 8, "department": " IT "},
    {"name": "sara", "status": "Absent", "hours": 0, "department": "HR"},
    {"name": "omar", "status": "present", "hours": 5, "department": "it"},
    {"name": "noor", "status": "Present", "hours": 9, "department": "Finance"},
    {"name": "khalid", "status": "Late", "hours": 6, "department": "IT"},
]
present_count = 0
not_present_count = 0
for employee in employees:
    name = employee["name"].strip().title()
    status = employee["status"].strip().lower()
    department = employee["department"].strip().lower()
    hours = employee["hours"]
    has_status = status == "present"
    working_hours = hours >= 6
    department_of = department == "it"
    if has_status and working_hours and department_of:
        print(name, "Present")
        present_count = present_count + 1
    else:
        print(name, "Not present")
        not_present_count = not_present_count + 1
print("Total present:", present_count)
print("Total Not present:", not_present_count)
print("Attendance checking finished")
