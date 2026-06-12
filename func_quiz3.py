def gym_membership_check(
    member, blocked, is_active, is_paid, age, has_id_card, is_verified
):
    if (
        not blocked
        and is_active
        and is_paid
        and 16 <= age <= 60
        and (has_id_card or is_verified)
    ):
        print(member, "gym entry allowed")
    else:
        print(member, "gym entry denied")


gym_membership_check("Ali", False, True, True, 25, False, True)
