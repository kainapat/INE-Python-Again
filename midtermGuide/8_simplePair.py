def simplePair(arr, n):
    s = set()  
    
    for num in arr:
        if n % num == 0 and n // num in s:
            return [num, n // num]
        s.add(num)  
    return None  

print(simplePair([1, 2, 3], 3))  
print(simplePair([1, 2, 3], 6))  
print(simplePair([1, 2, 3], 9))  
