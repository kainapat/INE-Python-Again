def sumTwoSmallestNums(arr):
    
    positive_nums = sorted([num for num in arr if num > 0])
    
    if len(positive_nums) >= 2: 
        return positive_nums[0] + positive_nums[1]
    else:
        return 0
    
print(sumTwoSmallestNums([19, 5, 42, 2, 771]))
print(sumTwoSmallestNums([10, 343445353, 3453445, 3453545353453]))
print(sumTwoSmallestNums([2, 9, 6, -1]))
print(sumTwoSmallestNums([879, 953, 694, -847, 342, 221, -91, -723, 791, -587]))
print(sumTwoSmallestNums([3683, 2902, 3951, -475, 1617, -2385]))
