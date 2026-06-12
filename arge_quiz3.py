def freelancer_pay(*args):
    total = sum(args)
    minimum = min(args)
    maximum = max(args)
    if total > 10000:
        final_payout = total + (total * 0.25)
    elif 4000 <= total <= 8000:
        final_payout = total + (total * 0.15)
    else:
        final_payout = total + (total * 0.05)
    return total, minimum, maximum, final_payout


print(freelancer_pay(1000, 2000, 3000, 4000))
