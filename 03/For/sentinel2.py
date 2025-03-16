rows = int(input('How many rows?: '))
columns = int(input('How many columns?: '))

for i in range(rows):
    for j in range(columns):
        print("*", end=" ")
    print(" ")

'''
output ที่ได้จากการรันโปรแกรมนี้จะเป็นสี่เหลี่ยมมีรูปแบบด้วยเครื่องหมาย (*) ตามที่ผู้ใช้ป้อนเข้ามาใน rows และ columns
'''