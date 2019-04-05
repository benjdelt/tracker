from math import ceil
from time import time


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


def compute_time(start, recorded_time=0):
    return recorded_time + ceil(time() - start)


def get_time_string(start, recorded_time=0):
    count = compute_time(start, recorded_time)
    return f"{format_time(count)}"
