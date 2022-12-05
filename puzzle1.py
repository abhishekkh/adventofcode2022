# Read the input file line by line and start the count
# If line is empty rollup count and add to an array
# find max value in array


def main():
    calories = 0
    elves_calories = []
    with open("puzzle1_input") as f:
        for line in f:
            if line.strip() != "":
                calories = calories + int(line.strip())
            else:
                elves_calories.append(calories)
                calories = 0

    print("max calorie is: ", max(elves_calories))

    # puzzle 2
    elves_calories.sort(reverse=True)
    print("top 3 total is: ", elves_calories[0] + elves_calories[1] + elves_calories[2])


if __name__ == "__main__":
    main()
