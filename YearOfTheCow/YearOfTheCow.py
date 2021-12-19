"""
Problem Year Of The Cow
USACO Competition Febuary, 2021
This problem took me  minutes, and  seconds to solve

Code from Aditya Rao U (ARJPEG), 2021
"""

calender = ["Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"]
cows = {"Bessie": ["Ox", 0]}

numberOfRelations = int(input())

for i in range(numberOfRelations):
    rel = input().split()

    cn = rel[0]

    print(rel)