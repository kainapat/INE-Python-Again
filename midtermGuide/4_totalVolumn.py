def totalVolume(*boxes):
    total = 0
    for box in boxes:
        volume = box[0] * box[1] * box[2]
        total += volume
    return total


print(totalVolume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]))
print(totalVolume([2, 2, 2], [2, 1, 1]))
print(totalVolume([1, 1, 1]))
