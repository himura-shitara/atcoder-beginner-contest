import math

x1, y1, x2, y2 = map(int, input().split())

if x1 == x2 and y1 == y2:
    print("Yes")
    exit()
if math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) > 5:
    print("No")
    exit()

if x1 > x2:
    x1, x2 = x2, x1
if y1 > y2:
    y1, y2 = y2, y1


def is_yes():
    for x in range(x1 - 2, x2 + 2):
        for y in range(y1 - 2, y2 + 2):
            if abs(x - x1) + abs(y - y1) == 3 and x != x1 and y != y1:
                if abs(x - x2) + abs(y - y2) == 3 and x != x2 and y != y2:
                    return "Yes"
    return "No"


print(is_yes())
