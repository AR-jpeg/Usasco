with open('blocks.in') as f:
    boards = [t.strip('\n').split(' ') for t in f.readlines()][1:]


base = ""
alphabet = map(chr, range(97, 123))


def findMinimumLetters(board):
    minLetters = {}

    for word in board:
        for letter in word:
            if letter not in minLetters:

                minLetters[letter] = max(
                    board[0].count(letter), board[1].count(letter))

    return minLetters


for board in boards:
    m = findMinimumLetters(board)  # fox box -> {f: 1, o:1, x:1, b:1}

    for key in m:
        base += key * m[key]

base = ''.join(sorted(base))

with open('blocks.out', 'w') as f:

    for letter in alphabet:
        f.write(str(base.count(letter)) + '\n')
