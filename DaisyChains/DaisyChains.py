"""
Problem Daisy Chains
USACO Competition December, 2020
This problem took me 15 minutes, and 17 seconds to solve

Code from Aditya Rao U (ARJPEG), 2021
"""



numberOfPhotosWithAnAverageFlower = 0

n = int(input())
flowers = list(map(int, input().split()))

for i in range(len(flowers)):
    for j in range(i, len(flowers)):
        sumOfFlowerPetals = sum(flowers[i:j+1])

        print((i, j+1), "->", flowers[i:j+1], "sum:", sumOfFlowerPetals)

        if sumOfFlowerPetals/len(flowers[i:j+1]) in flowers[i:j+1]:
            numberOfPhotosWithAnAverageFlower += 1



print(numberOfPhotosWithAnAverageFlower)
