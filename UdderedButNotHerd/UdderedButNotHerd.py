"""
Problem Uddered But Not Herd
USACO Competition January, 2021
This problem took me  minutes, and  seconds to solve

Code from Aditya Rao U (ARJPEG), 2021
"""

cowphabet = list(input())
word = input()


currentLetterIndex = 0
numberOfTimesCowphabetHummed = 1

for letter in word:
    indexOfLetter = cowphabet.index(letter)

    if indexOfLetter < currentLetterIndex:
        numberOfTimesCowphabetHummed += 1
    elif indexOfLetter == currentLetterIndex:
        numberOfTimesCowphabetHummed += 1

    currentLetterIndex = indexOfLetter

print(numberOfTimesCowphabetHummed)
