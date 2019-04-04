from math import ceil
from time import sleep, time


def pad_zero(n):
    return f"0{n}" if n < 10 else f"{n}"


def format_time(seconds):
    if seconds < 60:
        return f"{seconds}"
    if seconds < 3600:
        return f"{seconds // 60}:{pad_zero(seconds % 60)}"
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = ((seconds % 3600) % 60)
    return f"{hours}:{pad_zero(minutes)}:{pad_zero(seconds)}"


def get_time(start):
    count = ceil(time() - start)
    return f"{format_time(count)}"


if __name__ == '__main__':
    start = time()
    while True:
        output = get_time(start)
        sleep(1)
        print(output, end="\r")
