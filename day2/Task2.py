score = 0

with open('Dataset.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        if line == "A X\n":
            score += 3
        elif line == "A Y\n":
            score += 4
        elif line == "A Z\n":
            score += 8
        elif line == "B X\n":
            score += 1
        elif line == "B Y\n":
            score += 5
        elif line == "B Z\n":
            score += 9
        elif line == "C X\n":
            score += 2
        elif line == "C Y\n":
            score += 6
        elif line == "C Z\n":
            score += 7
        elif line == "A Z":
            score += 8
    print(score)