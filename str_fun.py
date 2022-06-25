#documentation or___init.py

def count_upper(st):
    count = 0
    for c in st:
        if c.isupper():
            count += 1

    return count


def has_digit(st):
    for c in st:
        if c.isdigit():
            return True

    return False