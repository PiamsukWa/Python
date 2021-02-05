#Python Conditional Statements : loop
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
