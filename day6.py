def prod(list: list[int]):
    result = 1
    for num in list:
        result *= num

    return result


def first():
    columns = []
    operations = []

    with open("input6") as file:
        # init
        columns = [[int(num)] for num in next(file).strip().split()]

        for row in file:
            if not row[0].isnumeric():
                operations = row.split()
                break
            for idx, num in enumerate(row.split()):
                columns[idx].append(int(num))

    column_sums = []
    for idx, column in enumerate(columns):
        if operations[idx] == '+':
            column_sums.append(sum(column))
        else:
            column_sums.append(prod(column))

    return sum(column_sums)


def second():
    columns = []
    operations = []

    with open("input6") as file:
        for row in file:
            if not row.strip()[0].isnumeric():
                operations = row.strip().split()
                break
            columns.append(row.strip('\n'))

    column_sums = 0
    current_column = []
    column_idx = len(columns[0].split()) - 1
    for idx in range(len(columns[0]) - 1, -1, -1):
        sub_column = ''.join([row[idx] for row in columns])
        sub_column_sum = 0 if sub_column.strip() == '' else int(sub_column)

        if sub_column_sum == 0:
            if operations[column_idx] == '+':
                column_sums += sum(current_column)
            else:
                column_sums += prod(current_column)
            column_idx -= 1
            current_column = []
        else:
            current_column.append(sub_column_sum)

    # last sub_column
    if operations[column_idx] == '+':
        column_sums += sum(current_column)
    else:
        column_sums += prod(current_column)

    return column_sums


print(first())
print(second())
