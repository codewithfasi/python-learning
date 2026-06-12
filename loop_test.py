scores = [45, 80, 60, 30, 95, 55, 70]
passed_count = 0
failed_count = 0

for score in scores:
    if score >= 60:
        print(score, "Pass")
        passed_count = passed_count + 1
    else:
        print(score, "Fail")
        failed_count = failed_count + 1
print("Total Passed:", passed_count)
print("Total Failed:", failed_count)
print("Checking finished")
