def salary_report(*args):
    total = sum(args)
    maximum = max(args)
    minimum = min(args)

    if total > 10000:
        final_salary = total + (total * 0.15)
    elif 5000 <= total <= 10000:
        final_salary = total + (total * 0.10)
    else:
        final_salary = total

    return total, maximum, minimum, final_salary


print(salary_report(2000, 3000, 4000, 5000))
