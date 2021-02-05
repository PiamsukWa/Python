#โปรแกรมตัวอย่าง
"""import os
choice = 0
filename = " "

def menu():
    global choice
    print("Menu\n 1.Open Exporer \n 2.Open Notepad\n 3.Exit ")
    choice = input("Select Menu : ")

""'def opennotepad():
    filename = "C:\Windows\\notepad.exe"
    print("Menorandum writing %s" %filename)
    os.system(filename)

def openexplorer():
    filename = "C:\Windows\\explorer.exe"
    print("search %s" %filename)
    os.system(filename)

while True:
    menu()
    if choice == "1" :
        openexplorer()
    elif choice == "2" :
        opennotepad()
    else:
        break"""


#แบบฝึกหัดที่ 4.1 


def menu():
    print("Menu\n 1.แสดงรายการสินค้า \n 2.หยิบสินค้าเข้าตะกร้า\n 3.แสงจำนวนและราคาของสินค้าที่หยิบ\n 4. หยิบสินค้าออกจากตะกร้า\n 5. ปิดโปรแกรม ")
    choice = int(input('กรุณาเลือกทำรายการ : '))

def เลือกรายการสินค้า():
    print("1.vans\n 2.adidas\n 3.converse\n 4.nike\n 5.lacost\n")
    choice = int(input("เลือกหยิบสินค้าหมายเลข : "))

print("-"*50)
print("-------- Bombam Sneaker -----")
print("-"*50)
menu()
เลือกรายการสินค้า()
