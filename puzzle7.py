def get_tuples(pair: list) -> (tuple,tuple):
    elf_1 = pair[0].split("-")
    l1 = int(elf_1[0])
    r1 = int(elf_1[1])
    t1 = (l1, r1)

    elf_2 = pair[1].split("-")
    l2 = int(elf_2[0])
    r2 = int(elf_2[1])
    t2 = (l2, r2)

    return t1, t2


def is_complete_overlap(pair: list) -> bool:
    t1, t2 = get_tuples(pair)
    l1 = t1[0]
    r1 = t1[1]
    l2 = t2[0]
    r2 = t2[1]
    return l2 >= l1 and r2 <= r1 or l1 >= l2 and r1 <= r2


def is_any_overlap(pair: list) -> bool:
    t1, t2 = get_tuples(pair)
    l1 = t1[0]
    r1 = t1[1]
    l2 = t2[0]
    r2 = t2[1]
    return (l1 <= l2 and r1 >= l2) or (l2 <= l1 and r2 >= l1)


def puzzle7():
    total_overlap_count = 0
    any_overlap_count = 0
    with open("puzzle7_input") as f:
        for line in f:
            ranges = line.strip().split(",")
            pair = []
            pair.append(ranges[0])
            pair.append(ranges[1])
            if is_complete_overlap(pair):
                total_overlap_count += 1
            if is_any_overlap(pair):
                any_overlap_count += 1

    print("complete overlapping count is: ", total_overlap_count)
    print("any overlap count is: ", any_overlap_count)


if __name__ == "__main__":
    puzzle7()
