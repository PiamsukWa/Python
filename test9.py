#Python Conditional Statements if else
print("#"*50)
print("เลือกเมนูเพื่อทำรายการ")
print("#"*50)
print(" กด 1 เลือกจ่ายเพิ่ม ")
print(" กด 2 เลือกแบบเหมาจ่าย \n ")
a = int(input("กดตัวเลขที่ต้องการ : "))
b = int(input("กรุณากรอกระยะทาง : "))
if a == 1 :
    if b <= 25 :
        print(" ค่าใช้จ่าย รวมทั้งหมด 25 บาท ")
    else :
        print(" ค่าใช้จ่าย รวมทั้งหมด 80 บาท ")
elif a == 2 :
    if b <= 25 :
        print(" ค่าใช้จ่าย รวมทั้งหมด 25 บาท ")
    else :
        print(" ค่าใช้จ่าย รวมทั้งหมด 55 บาท ")
