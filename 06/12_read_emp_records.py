'''กันลืม อ่าน Comment ด้วย!!!!!'''
def main():
    #เปิดไฟล์ employees.txt สำหรับอ่าน
    emp_file = open('employees.txt', 'r')
    #อ่านภายในไฟล์ทั้งหมดและเก็บไว้ในรายการ (list)
    lines = emp_file.readlines()

    #คำนวณจำนวนพนักงานทั้งหมดโดยหารจำนวนบรรทัดในไฟล์ด้วย 3
    num_emps = len(lines) // 3

    #ใช้ลูป for เพื่อวนลูปตามจำนวนพนักงานทั้งหมด โดยคำนวณ index ของ name, ID และ dept
    for count in range(num_emps):
        name = lines[count * 3].strip()
        id_num = lines[count * 3 + 1].strip()
        dept = lines[count * 3 + 2].strip()

        #แสดง name, ID และ dept
        print('Name:', name)
        print('ID:', id_num)
        print('Dept:', dept)
        print()

    #ปิดไฟล์ employees.txt 
    emp_file.close()

main()