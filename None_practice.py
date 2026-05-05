_min = None
for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    if _min is None or num < _min:
        _min = num

print(_min)