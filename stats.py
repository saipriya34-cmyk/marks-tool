"""Statistics for a list of marks."""

def average(marks):
    if not marks:
        return 0.0
    return sum(marks) / len(marks)

def highest(marks):
    return max(marks)

def lowest(marks):
    return min(marks)

def pass_count(marks, pass_mark):
    return len([mark for mark in marks if mark >= pass_mark])

def percentage(marks):
    return round(average(marks), 2)

def lowest(marks):
    return min(marks)
# TODO: check pass mark validation
