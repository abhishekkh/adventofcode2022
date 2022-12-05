def find_priority(input: str) -> int:
    if input.islower():
        priority = ord(input) - ord("a") + 1
        return priority

    if input.isupper():
        priority = ord(input) - ord("A") + 1 + 26
        return priority


def puzzle_5():
    total_priority = 0
    with open("puzzle5_input") as f:
        for line in f:
            items = list(line.strip())
            pack_1 = items[: len(items) // 2]
            pack_2 = items[len(items) // 2 :]
            common_item_set = set(pack_1) & set(pack_2)
            common_item = common_item_set.pop()
            total_priority += find_priority(common_item)

    print("total priority is: ", total_priority)


def puzzle_6():
    total_priority = 0
    groups = []
    with open("puzzle5_input") as f:
        idx = 0
        for line in f:
            items = list(line.strip())
            groups.append(items)
            idx += 1
            if idx == 3:
                common_item_set = set(groups[0]) & set(groups[1]) & set(groups[2])
                common_item = common_item_set.pop()
                total_priority += find_priority(common_item)
                idx = 0
                groups.clear()

    print("total priority is: ", total_priority)


def main():
    puzzle_5()
    puzzle_6()


if __name__ == "__main__":
    main()
