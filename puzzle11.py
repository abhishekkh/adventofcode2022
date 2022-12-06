def puzzle11(window_size: int):
    with open("puzzle11_input") as f:
        input = f.readline().strip()

    datastream = list(input)
    left = 0
    right = 0

    seen = []

    while left <= right:
        if datastream[right] not in seen:
            seen.append(datastream[right])
            right += 1
            if len(seen) == window_size:
                break
        else:
            while datastream[right] in seen:
                seen.remove(datastream[left])
                left += 1

    print("character count is", right)


if __name__ == "__main__":
    puzzle11(4)
    puzzle11(14) #puzzle12
