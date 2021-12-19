"""
Problem Lonely Photo
USACO Competition December, 2021
This problem took me  minutes, and  seconds to solve

Code from Aditya Rao U (ARJPEG), 2021
"""


n = int(input())
cows = input()
lonelyPhotos = 0

for i in range(0, n-2):
    for j in range(i+3, n+1):
        if cows[i:n+1].count("G") == 0 or cows[i:n+1].count("H") == 0:
            break

        photo = cows[i:j]

        # print(i, j, photo)

        if photo.count("G") > 1 and photo.count("H") > 1:
            break

        if photo.count("G") == 1 or photo.count("H") == 1:
            lonelyPhotos += 1
            # print("Adding one to lonely cows,", photo.count(
            #     "G"), "G and", photo.count("H"), "H")

        # print()
        # print(photo, lonelyPhotos)


# print(photos)
print(lonelyPhotos)
