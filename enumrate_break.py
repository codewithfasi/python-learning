attempts = ["success", "success", "blocked", "success"]
for index, attempt in enumerate(attempts):
    if attempt == "blocked":
        print("Blocked found at index:", index)
        print("Attempt result:", attempt)
        break