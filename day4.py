def populate_diagram(input: str):
    diagram = []

    with open(input) as file:
        first_row = next(file).strip()
        buffer_row = '.' * (len(first_row) + 2)
        # padding
        diagram.append(list(buffer_row))
        diagram.append(list('.' + first_row + '.'))

        for row in file:
            diagram.append(list('.' + row.strip() + '.'))

        diagram.append(list(buffer_row))

    return diagram


def first(input: str):
    accessible_rolls = 0
    diagram = populate_diagram(input)
    row_len = len(diagram)
    col_len = len(diagram[0])
    check_mask = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for i in range(1, col_len - 1):
        for j in range(1, row_len - 1):
            roll_count = 0

            if diagram[i][j] != '@':
                continue

            for rel_i, rel_j in check_mask:
                if diagram[i + rel_i][j + rel_j] == '@':
                    roll_count += 1

            if roll_count < 4:
                accessible_rolls += 1

    return accessible_rolls

def second(input: str):
    accessible_rolls, updated_accessible_rolls = 0, 0
    iteration = 0
    diagram = populate_diagram(input)
    row_len = len(diagram)
    col_len = len(diagram[0])
    check_mask = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    while updated_accessible_rolls != accessible_rolls or updated_accessible_rolls == 0:
        iteration += 1
        accessible_rolls = updated_accessible_rolls

        for i in range(1, col_len - 1):
            for j in range(1, row_len - 1):
                roll_count = 0

                if diagram[i][j] != '@':
                    continue

                for rel_i, rel_j in check_mask:
                    if diagram[i + rel_i][j + rel_j] == '@' or diagram[i + rel_i][j + rel_j] == str(iteration):
                        roll_count += 1

                if roll_count < 4:
                    updated_accessible_rolls += 1
                    diagram[i][j] = str(iteration)

    return accessible_rolls



#print(first("input4"))
print(second("input4"))
