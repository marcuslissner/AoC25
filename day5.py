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

    # 1. save all numbers as (value, edge_type) tuples
    with open("input5") as file:
        row = next(file)
        while row != "\n":
            lower, upper = row.split('-')
            edges.append((int(lower), '('))
            edges.append((int(upper), ')'))
            row = next(file)

    # 2. sort by key
    edges = sorted(edges)

    id_count = 0
    lower = 0
    depth = -1
    # 3. count parenthesis depth
    for edge, edge_type in edges:
        # new range case
        if depth == -1:
            lower = edge
            depth = 1
            continue
        if edge_type == '(':
            depth += 1
        if edge_type == ')':
            depth -= 1
        # end of range, reset depth
        if depth == 0:
            id_count += edge - lower + 1
            depth = -1

    return id_count


print(first())
print(second())
