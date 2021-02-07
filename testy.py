import rozwiazanie_1
import rozwiazanie_2
import random
import string


def non_number_passed(rozw, string):
    if rozw == 1:
        assert rozwiazanie_1.kontenery(string)[0] == -1
    else:
        assert rozwiazanie_2.kontenery(string)[0] == -1


def number_under_1(rozw, N):
    if rozw == 1:
        assert rozwiazanie_1.kontenery(N)[0] == -3
    else:
        assert rozwiazanie_2.kontenery(N)[0] == -3


def number_above_100(rozw, N):
    if rozw == 1:
        assert rozwiazanie_1.kontenery(N)[0] == -2
    else:
        assert rozwiazanie_2.kontenery(N)[0] == -2


def number_not_int(rozw, N):
    if rozw == 1:
        assert rozwiazanie_1.kontenery(N)[0] == -1
    else:
        assert rozwiazanie_2.kontenery(N)[0] == -1


def lower_border(rozw):
    if rozw == 1:
        assert rozwiazanie_1.kontenery(1) == {"big boxes": 0, "medium boxes": 0, "small boxes": 1, "summary box": 0}
    else:
        assert rozwiazanie_2.kontenery(1) == {"big boxes": 0, "medium boxes": 0, "small boxes": 1, "summary box": 0}


def higher_border(rozw):
    if rozw == 1:
        assert rozwiazanie_1.kontenery(100) == {"big boxes": 11, "medium boxes": 0, "small boxes": 1, "summary box": 4}
    else:
        assert rozwiazanie_1.kontenery(100) == {"big boxes": 11, "medium boxes": 0, "small boxes": 1, "summary box": 4}


def number_diff_in_rozwaizanie_1_and_rozwiazanie_2_10_12(rozw, N=random.randint(10, 12)):
    if rozw == 1:
        assert rozwiazanie_1.kontenery(N) == {"big boxes": 1, "medium boxes": 0, "small boxes": 1, "summary box": 1}
    else:
        assert rozwiazanie_1.kontenery(N) == {"big boxes": 0, "medium boxes": 2, "small boxes": 0, "summary box": 1}


def number_diff_in_rozwaizanie_1_and_rozwiazanie_2_13_15(rozw, N=14):
    if rozw == 1:
        assert rozwiazanie_1.kontenery(N) == {"big boxes": 1, "medium boxes": 1, "small boxes": 0, "summary box": 1}
    else:
        assert rozwiazanie_1.kontenery(N) == {"big boxes": 0, "medium boxes": 2, "small boxes": 0, "summary box": 1}


def number_in_middle(rozw, N):
    if rozw == 1:
        assert rozwiazanie_1.kontenery(N) == {"big boxes": 5, "medium boxes": 1, "small boxes": 0, "summary box": 2}
    else:
        assert rozwiazanie_1.kontenery(N) == {"big boxes": 5, "medium boxes": 1, "small boxes": 0, "summary box": 2}


def new_summaru_bottom_boundry(rozw, N=64):
    if rozw == 1:
        assert rozwiazanie_1.kontenery(N) == {"big boxes": 7, "medium boxes": 0, "small boxes": 1, "summary box": 3}
    else:
        assert rozwiazanie_1.kontenery(N) == {"big boxes": 7, "medium boxes": 0, "small boxes": 1, "summary box": 3}


def new_summaru_upper_boundry(rozw, N=63):
    if rozw == 1:
        assert rozwiazanie_1.kontenery(N) == {"big boxes": 7, "medium boxes": 0, "small boxes": 0, "summary box": 2}
    else:
        assert rozwiazanie_1.kontenery(N) == {"big boxes": 7, "medium boxes": 0, "small boxes": 0, "summary box": 2}


if __name__ == '__main__':
    print(5 / 4)
    for j in range(1, 2):
        for i in range(5):
            non_number_passed(j, ''.join(
                random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(0, 20))))
            number_under_1(j, random.randint(-999, 0))
            number_above_100(j, random.randint(101, 999))
            non_number_passed(j, float(f"{random.randint(0, 999)}.{random.randint(0, 999)}"))
            lower_border(j)
            higher_border(j)
            number_diff_in_rozwaizanie_1_and_rozwiazanie_2_10_12(j)
            number_diff_in_rozwaizanie_1_and_rozwiazanie_2_13_15(j)
            number_in_middle(j, 50)
            new_summaru_bottom_boundry(j)
