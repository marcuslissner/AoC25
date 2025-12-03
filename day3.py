from operator import index


def get_joltage(battery_bank: list[int]):
    tens_val = battery_bank[0]
    tens_idx = 0
    ones_val = battery_bank[1]
    ones_idx = 1
    last_idx = len(battery_bank) - 1

    for idx, battery in enumerate(battery_bank):
        if idx < last_idx and idx > tens_idx and battery > tens_val:
            tens_val = battery
            tens_idx = idx
            ones_val = battery_bank[idx + 1]
            ones_idx = idx + 1
        if idx > 0 and idx > ones_idx and idx > tens_idx and battery > ones_val:
            ones_val = battery
            ones_idx = idx

    return int(str(tens_val) + str(ones_val))


def first():
    total_joltage = 0
    with open("input3") as file:
        for row in file:
            battery_bank = list(map(lambda battery: int(battery), row.strip()))
            total_joltage += get_joltage(battery_bank)

    return total_joltage


def populate_candidates(chosen_batteries: list[int],
                        init_idx: int,
                        abs_all_idx: int,
                        chosen_num_batteries: int):
    for idx in range(init_idx, chosen_num_batteries):
        chosen_batteries[idx] = abs_all_idx + (idx - init_idx)

    return chosen_batteries


def get_super_joltage(all_batteries: list[int]):
    chosen_num_batteries = 12
    last_idx = len(all_batteries) - 1
    # pre-populate
    chosen_batteries = list(range(chosen_num_batteries))

    for all_idx in range(len(all_batteries)):
        for chosen_idx, existing_idx in enumerate(chosen_batteries):
            abs_all_idx = all_idx + chosen_idx

            # break early
            out_of_bounds = abs_all_idx + (chosen_num_batteries - chosen_idx - 1) > last_idx
            if out_of_bounds:
                break

            # check if new index is legal
            idx_in_order = (abs_all_idx > existing_idx and
                            (chosen_idx == 0 or abs_all_idx > chosen_batteries[chosen_idx - 1]))
            # check if new value is higher
            higher_value = all_batteries[abs_all_idx] > all_batteries[existing_idx]

            if idx_in_order and higher_value:
                # re-populate everything after chosen_idx
                populate_candidates(chosen_batteries, chosen_idx, abs_all_idx, chosen_num_batteries)

    return int(''.join(str(all_batteries[idx]) for idx in chosen_batteries))


def second():
    total_joltage = 0
    with open("input3") as file:
        for row in file:
            battery_bank = list(map(lambda battery: int(battery), row.strip()))
            total_joltage += get_super_joltage(battery_bank)

    return total_joltage


print(first())
print(second())
