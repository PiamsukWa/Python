#Python Conditional Statements : loop
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
    print("\n ทำคำสั่งถัดไป")