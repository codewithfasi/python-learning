payments = ["paid", "paid", "failed", "paid", "pending"]
for payment in payments:
    print("Checking payment:", payment)
    if payment == "failed":
        print("Failed payment found")
        break
