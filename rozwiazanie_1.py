def kontenery(N):
    big_box = 0
    medium_box = 0
    small_box = 0
    number_full = N / 9
    number_rest = N % 9

    if type(N) is not int:
        return [-1, "Not int number"]
    elif N > 100:
        return [-2, "Size of delivery to big"]
    elif N < 1:
        return [-3, "Size of delivery to small"]

    if number_full > 0:
        big_box = int(number_full)

    if 0 < number_rest <= 3:
        small_box = 1
    elif 3 < number_rest <= 6:
        medium_box = 1
    elif 6 < number_rest <= 9:
        big_box += 1
    summary_box = big_box + medium_box + small_box
    if summary_box == 1:
        summary_box = 0
    else:
        summary_box = int(summary_box / 4 + 1)

    return {"big boxes": big_box, "medium boxes": medium_box, "small boxes": small_box, "summary box": summary_box}

