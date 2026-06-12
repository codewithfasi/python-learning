def payroll(*args):
    grand_total = 0

    for employee in args:
        print(employee)

        employee_total = 0
        for salary in employee:
            employee_total += salary

        print(employee_total)
        grand_total += employee_total

    print("Grand Total:", grand_total)


payroll((2000, 3000, 4000), (5000, 6000), (1000, 1500, 2500))
