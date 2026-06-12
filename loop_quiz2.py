statuses = ["paid", "unpaid", "paid", "pending", "paid", "unpaid"]
paid_count = 0
not_paid_count = 0

for status in statuses:
    if status == "paid":
        print(status, "Access allowed")
        paid_count = paid_count + 1
    else:
        print(status, "Access denied")
        not_paid_count = not_paid_count + 1
print("Total Paid:", paid_count)
print("Total not paid:", not_paid_count)
print("Registration checking finished")
