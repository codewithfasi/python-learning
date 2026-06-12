profile = {
    "name": "Faisal",
    "skills": ["Python", "HTML"],
    "details": {"city": "Riyadh", "level": "Beginner"},
}

backup = profile.copy()

profile["skills"].append("CSS")
profile["details"]["level"] = "Intermediate"
profile["name"] = "Ali"

print(profile)
print(backup)


word = "Code"

for letter in word:
    print("Letter:", letter)

print("Done")
print(letter)
