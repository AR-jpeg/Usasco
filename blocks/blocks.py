from typing import Dict, List


with open('blocks.in') as f:
    boards = [t.strip('\n').split(' ') for t in f.readlines()][1:]

    print(boards)


base = ""
alphabet = map(chr, range(97, 123))


def findMinimumLetters(board: List[str]) -> Dict[str, int]:
    minLetters: Dict[str, int] = {}

    for word in board:
        for letter in word:
            if letter not in minLetters:

                print(letter + ' not in minLetters yet, adding it ' + str(max(
                    board[0].count(letter), board[1].count(letter))))

                minLetters[letter] = max(
                    board[0].count(letter), board[1].count(letter))
            else:
                print(letter + ' is already in minLetters')

    return minLetters


for board in boards:
    m = findMinimumLetters(board)  # fox box -> {f: 1, o:1, x:1, b:1}

    for key in m:
        base += key * m[key]

base = ''.join(sorted(base))
print(base)

with open('blocks.out', 'w') as f:

    for letter in alphabet:
        f.write(str(base.count(letter)) + '\n')

    # alreadyWrittenLetters = []

    # for letter in base:
    #     if letter not in alreadyWrittenLetters:
    #         f.write(base.count(letter))

    #     alreadyWrittenLetters.append

    # f.write('\n')
