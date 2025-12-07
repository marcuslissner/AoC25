def first():
    split_count = 0

    with open("input7") as file:
        start_pos = next(file).find('S')
        current_beams = {start_pos}
        for row in file:
            next_beams = set()
            for beam in current_beams:
                if row[beam] == '^':
                    split_count += 1
                    next_beams.add(beam - 1)
                    next_beams.add(beam + 1)
                else:
                    next_beams.add(beam)

            current_beams = next_beams

    return split_count


print(first())
# print(second())
