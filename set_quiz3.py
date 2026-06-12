student_skills = ["Python", "HTML", "Python", "CSS", "HTML"]
new_skill = "Java"
more_skills = ["SQL", "CSS", "Python"]
unique_skills = set(student_skills)
unique_skills.add(new_skill)
unique_skills.update(more_skills)
print(unique_skills)
print(len(unique_skills))
