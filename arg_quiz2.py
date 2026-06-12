def order_analysis(*args):
    total = sum(args)
    maximum = max(args)
    minimum = min(args)

    if total > 3000:
        final_price = total - (total * 0.20)
    elif 1500 <= total <= 3000:
        final_price = total - (total * 0.10)
    else:
        final_price = total

    return total, maximum, minimum, final_price


print(order_analysis(400, 500, 4000))
