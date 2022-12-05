# read the file by line and for each line
# calculate the score
ROCK = 1
PAPER = 2
SCISSORS = 3

LOSS = 0
DRAW = 3
WIN = 6


def find_winner(p1: int, p2: int) -> int:
    P1_WIN = 1
    P2_WIN = 2
    NOWIN = 0

    if p1 is ROCK and p2 is ROCK:
        return NOWIN
    if p1 is ROCK and p2 is PAPER:
        return P2_WIN
    if p1 is ROCK and p2 is SCISSORS:
        return P1_WIN
    if p1 is PAPER and p2 is ROCK:
        return P1_WIN
    if p1 is PAPER and p2 is PAPER:
        return NOWIN
    if p1 is PAPER and p2 is SCISSORS:
        return P2_WIN
    if p1 is SCISSORS and p2 is ROCK:
        return P2_WIN
    if p1 is SCISSORS and p2 is PAPER:
        return P1_WIN
    if p1 is SCISSORS and p2 is SCISSORS:
        return NOWIN


def find_play(p1: int, result: int) -> int:
    P1_WIN = 1
    NO_WIN = 2
    P2_WIN = 3

    if p1 is ROCK and result is P1_WIN:
        return SCISSORS
    if p1 is ROCK and result is NO_WIN:
        return ROCK
    if p1 is ROCK and result is P2_WIN:
        return PAPER
    if p1 is PAPER and result is P1_WIN:
        return ROCK
    if p1 is PAPER and result is NO_WIN:
        return PAPER
    if p1 is PAPER and result is P2_WIN:
        return SCISSORS
    if p1 is SCISSORS and result is P1_WIN:
        return PAPER
    if p1 is SCISSORS and result is NO_WIN:
        return SCISSORS
    if p1 is SCISSORS and result is P2_WIN:
        return ROCK


def puzzle3_score():
    score = 0
    with open("puzzle3_input") as f:
        for line in f:
            play = line.split()
            # normalize the plays
            p1 = ord(play[0]) - ord("A") + 1
            p2 = ord(play[1]) - ord("X") + 1

            # find winner
            winner = find_winner(p1, p2)
            if winner == 2:
                score += WIN + p2
            if winner == 1:
                score += LOSS + p2
            if winner == 0:
                score += DRAW + p2

    print("final score is: ", score)

def puzzle4_score():
    score = 0
    result_arr = [ 0, 3, 6]
    with open("puzzle3_input") as f:
        for line in f:
            play = line.split()
            # normalize the plays
            p1 = ord(play[0]) - ord("A") + 1
            result = ord(play[1]) - ord("X") + 1

            # find play
            play = find_play(p1, result)
            score += result_arr[result - 1] + play

    print("final score is: ", score)

def main():
    puzzle3_score()
    puzzle4_score()


if __name__ == "__main__":
    main()
