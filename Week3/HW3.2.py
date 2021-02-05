print("กรุณากรอกจำนวนครั้งการรับค่า")
x = int(input("จำนวนครั้งที่รับค่า :"))
i=0
sum=0
while(i < x) :
    number = int(input("input number : "))
    i+=1
    sum = sum + number
print("ผลรวมค่าที่รับมาทั้งหมด :"+str(sum))