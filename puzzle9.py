# [P]     [C]         [M]
# [D]     [P] [B]     [V] [S]
# [Q] [V] [R] [V]     [G] [B]
# [R] [W] [G] [J]     [T] [M]     [V]
# [V] [Q] [Q] [F] [C] [N] [V]     [W]
# [B] [Z] [Z] [H] [L] [P] [L] [J] [N]
# [H] [D] [L] [D] [W] [R] [R] [P] [C]
# [F] [L] [H] [R] [Z] [J] [J] [D] [D]
#  1   2   3   4   5   6   7   8   9

stacks = []
stack1 = ["F", "H", "B", "V", "R", "Q", "D", "P"]
stacks.append(stack1)
stack2 = ["L", "D", "Z", "Q", "W", "V"]
stacks.append(stack2)
stack3 = ["H", "L", "Z", "Q", "G", "R", "P", "C"]
stacks.append(stack3)
stack4 = ["R", "D", "H", "F", "J", "V", "B"]
stacks.append(stack4)
stack5 = ["Z", "W", "L", "C"]
stacks.append(stack5)
stack6 = ["J", "R", "P", "N", "T", "G", "V", "M"]
stacks.append(stack6)
stack7 = ["J", "R", "L", "V", "M", "B", "S"]
stacks.append(stack7)
stack8 = ["D", "P", "J"]
stacks.append(stack8)
stack9 = ["D", "C", "N", "W", "V"]
stacks.append(stack9)


def move_container(to_move: int, from_s: int, to_s: int) -> None:
    for count in range(to_move):
        x = stacks[from_s - 1].pop()
        stacks[to_s - 1].append(x)


def move_container_stacks(to_move: int, from_s: int, to_s: int) -> None:
    stack_to_move = stacks[from_s - 1]
    # remove from older stack
    stacks[from_s - 1] = stack_to_move[0 : (len(stack_to_move) - to_move)]
    sub_stack = stack_to_move[(len(stack_to_move) - to_move) :]
    for container in sub_stack:
        stacks[to_s - 1].append(container)


def puzzle9():
    with open("puzzle9_input") as f:
        for line in f:
            input = line.strip().split()
            move_container(int(input[1]), int(input[3]), int(input[5]))
    for i in range(len(stacks)):
        print(stacks[i].pop())


def puzzle10():
    with open("puzzle9_input") as f:
        for line in f:
            input = line.strip().split()
            move_container_stacks(int(input[1]), int(input[3]), int(input[5]))
    for i in range(len(stacks)):
        print(stacks[i].pop())


if __name__ == "__main__":
    # puzzle9()
    puzzle10()
