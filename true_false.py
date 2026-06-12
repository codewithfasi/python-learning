student_name = "   aLi   "
email = "   ALI@GMAIL.COM   "
blocked = False
fee_paid = True
has_id = False
is_vip = True
score = 75
clean_email = email.strip().lower()

if (
    not blocked
    and fee_paid
    and (has_id or is_vip)
    and 50 <= score <= 100
    and clean_email.endswith("@gmail.com")
):
    print("Allowed")
else:
    print("Not Allowed")
