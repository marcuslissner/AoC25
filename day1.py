def first():
    current_position = 50
    zero_count = 0

    with open("input1") as instructions:
        for instruction in instructions:
            direction, *steps = instruction.strip()
            vector = -1 * int(''.join(steps)) if direction == 'L' else int(''.join(steps))

            current_position = (current_position + vector) % 100
            if current_position == 0:
                zero_count += 1

    return zero_count

def second():
    current_position = 50
    zero_count = 0

    with open("input1") as instructions:
        for instruction in instructions:
            direction, *steps = instruction.strip()
            numerical_direction = -1 if direction == 'L' else 1
            steps_count = int(''.join(steps))

            # flip circle if L movement
            if numerical_direction == -1:
                current_position = (100 - current_position) % 100

            crosses = (current_position + steps_count) // 100
            current_position = (current_position + steps_count) % 100

            # flip back if L movement
            if numerical_direction == -1:
                current_position = (100 - current_position) % 100

            zero_count += crosses

    return zero_count

print(first())
print(second())
