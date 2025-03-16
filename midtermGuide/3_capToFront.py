def capToFront(word):
    return ''.join(sorted(word, key=lambda x: x.islower()))


print(capToFront("hApPy"))    
print(capToFront("moveMENT"))  
print(capToFront("shOrtCAKE"))

