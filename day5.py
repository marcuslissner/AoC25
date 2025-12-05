def first():
    ranges = []
    fresh_count = 0

    with open("input5") as file:
        row = next(file)
        while row != "\n":
            lower, upper = row.split('-')
            ranges.append((int(lower), int(upper)))
            row = next(file)

        for row in file:
            for lower, upper in ranges:
                if lower <= int(row) <= upper:
                    fresh_count += 1
                    break

    return fresh_count


def second():
    edges = []

    with open("input5") as file:
        row = next(file)
        while row != "\n":
            lower, upper = row.split('-')
            edges.append((int(lower), '('))
            edges.append((int(upper), ')'))
            row = next(file)

    edges = sorted(edges)

    id_count = 0
    lower = 0
    level = -1
    for edge, edge_type in edges:
        # new range case
        if level == -1:
            lower = edge
            level = 1
            continue
        if edge_type == '(':
            level += 1
        if edge_type == ')':
            level -= 1
        if level == 0:
            id_count += edge - lower + 1
            level = -1

    return id_count


print(first())
print(second())
