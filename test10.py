#Python Conditional Statements : loops
''''print("#"*50)
print("กรุณากรอกจำนวนครั้งการรับค่า \n")
x = int(input("จำนวน : "))
i = 0
sum = 0
while(i<x):
    y = int(input("กรอกตัวเลข : "))
    i += 1
    sum = sum + y
print("ผลรวมคือ =" + str(sum))'''


#แบบฝึกหัดที่ 3.3
print(" "*50)
print("ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม \n")
food = []
i = 1
x = 0
y = 1
while(True):
    x = input(" อาหารสุดโปรดของคุณลำดับที่ " + str(i) +" คือ ")
    food.append(x)
    i += 1

    if x == "exit" :
        print("\n อาหารสุดโปรดของคุณมีดังนี้ ",end= "\n ")
        food.pop()
        break

for x in food :
    print(str(y)+"."+x,end="  ")
    y+=1 

'''
#แบบฝึกหัดที่ 3.4
a = []
while True :
    b = input("-----บ๋อมแบ๋มคาเฟ่-----\n เพิ่มข้อมูล [a]\n แสดงข้อมูล [s]\n ออกจากระบบ [x]\n")
    b = b.lower()
    if b== "a" :
        c = input("โปรดป้อนรายการลูกค้า(โต๊ะ:ชื่อ:เมนู) => ")
        a.append(c)
        print("\n******ข้อมูลได้เข้าสู่ระบบแล้ว******\n")
    elif b == "s" :
        print("{0:-<6}{0:-<10}{0:-<10}".format(""))
        print("{0:-<8}{1:-<10}{2:10}".format("โต๊ะ","ชื่อ","เมนู"))
        print("{0:-<6}{0:-<10}{0:-<10}".format(""))
        for d in a :
            e = d.split(":")
            print("{0[0]:<6}{0[1]:<10}{0[2]:<10}".format(e))
            continue
    elif b == "x" :
        break
    print("\n ทำคำสั่งถัดไป")'''