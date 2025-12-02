def find_all_symmetrical(lower: int, upper: int):
    range_sum = 0
    lower_str = str(lower)
    lower_len = len(lower_str)
    current = 0

    if lower_len % 2 == 0:
        first_half = lower_str[:(lower_len // 2)]
        current = int(first_half * 2)
        if current < lower:
            current = int(str(int(first_half) + 1) * 2)
    else:
        current = int(('1' + '0' * ((lower_len + 1) // 2 - 1)) * 2)

    while current <= upper:
        range_sum += current
        current = int(str(int(str(current)[:(len(str(current)) // 2)]) + 1) * 2)

    return range_sum


def first():
    total_sum = 0
    with open("input2") as file:
        ranges = file.read().rstrip().split(',')
        for range in ranges:
            lower, upper = range.split('-')
            total_sum += find_all_symmetrical(int(lower), int(upper))

    return total_sum


def find_all_repeating(lower: int, upper: int):
    range_sum = 0

    for current in range(lower, upper + 1):
        current_str = str(current)
        current_len = len(current_str)
        for chunk_count in range(2, current_len + 1):
            if current_len % chunk_count != 0:
                continue
            chunk_size = current_len // chunk_count
            chunks = [current_str[i:i + chunk_size] for i in range(0, current_len, chunk_size)]
            if len(chunks) > 1 and len(set(chunks)) == 1:
                range_sum += current
                break

    return range_sum


def second():
    total_sum = 0
    with open("input2") as file:
        ranges = file.read().rstrip().split(',')
        for range in ranges:
            lower, upper = range.split('-')
            total_sum += find_all_repeating(int(lower), int(upper))

    return total_sum


print(first())
print(second())
