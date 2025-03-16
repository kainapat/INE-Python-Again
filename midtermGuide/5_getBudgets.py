def getBudgets(people):
    total_budget = 0
    for person in people:
        if 'budget' in person:
            total_budget += person['budget']
    return total_budget

# Examples
people1 = [
    { 'name': "John", 'age': 21, 'budget': 23000 },
    { 'name': "Steve", 'age': 32, 'budget': 40000 },
    { 'name': "Martin", 'age': 16, 'budget': 2700 }
]

people2 = [
    { 'name': "John", 'age': 21, 'budget': 29000 },
    { 'name': "Steve", 'age': 32, 'budget': 32000 },
    { 'name': "Martin", 'age': 16, 'budget': 1600 }
]

result1 = getBudgets(people1)
result2 = getBudgets(people2)

print(result1)  # Output: 65700
print(result2)  # Output: 62600
