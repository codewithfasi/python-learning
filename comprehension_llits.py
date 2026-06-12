student_names = [" sara ", "ALI", " omar", "MONA "]
scores = [50, 60, 70, 80]
courses = [" python basics ", "HTML", " data science ", "JAVA"]
emails = [" ALI@GMAIL.COM ", " Sara@Yahoo.Com ", " OMAR@GMAIL.COM "]
files = [" CV.PDF ", " Photo.JPG", " report.DOCX ", "notes.txt"]

clean_names = [student_name.strip().title() for student_name in student_names]
updated_scores = [score + 10 for score in scores]
clean_courses = [course.strip().title() for course in courses]
clean_emails = [email.strip().lower() for email in emails]
clean_files = [file.strip().lower() for file in files]

print(clean_names)
print(updated_scores)
print(clean_courses)
print(clean_emails)
print(clean_files)
