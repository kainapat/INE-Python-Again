keep_going = "y"

while keep_going == 'y':
        wholesale = float(input("Enter the item's wholesale cost: "))
        retail_price = wholesale * 2.5
        print("Retail price: ${:.2f}".format(retail_price))
        keep_going = input("Do you have another item?" + \
                       "(Enter y for yes): ")
        
'''
โปรแกรมนี้จะวนลูปต่อไปเรื่อยๆ ในกรณีที่ผู้ใช้ป้อน "y" ในคำถาม หากต้องการหยุดทำงานและออกจากโปรแกรม ผู้ใช้ควรป้อนค่าที่ไม่ใช่ "y" หรือตัวอักษรอื่นใดนอกเหนือจาก "y"
'''