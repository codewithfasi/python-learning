scores = (45, 80, 66, 90, 30, 75)
passed_score = []
failed_score = []
passed_count = 0
failed_count = 0
for score in scores:
    if score >= 50:
        passed_score.append(score)
        passed_count = passed_count + 1
    else:
        failed_score.append(score)
        failed_count = failed_count + 1
print(passed_score)
print(failed_score)
print(passed_count)
print(failed_count)
   





