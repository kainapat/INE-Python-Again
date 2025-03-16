while True:
    s = input("Enter a string: ")
    if not s:
        break
    i, _, d = s.partition('.')
    i = i.lstrip('0') or '0'
    d = d.rstrip('0')
    result = i + ('.' + d if d else '')
    print(f"The input string is {s} output is {result}")
