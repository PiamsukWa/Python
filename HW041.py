listshop=[0,0,0,0,0]
cost=[2300,1400,2100,1990,2400]
def menu():
	global choice
	print("-------Bombam Sneaker-------\n 1. แสดงรายการสินค้า\n 2. หยิบสินค้าใส่ตะกร้า\n 3. แสดงรายการจำนวนและราคาสินค้าที่หยิบ\n 4. หยิบสิค้าออกจากตะกร้า\n 5. ปิดโปรแกรม ")
	choice = input("กรุณาเลือกทำรายการ : ")

def costmenu():
    print("\t รายการสินค้า")
    print("-"*30)
    print("\t1.nike cortez ราคา 2300 บาท")
    print("\t2.adidas superstar ราคา 1400 บาท")
    print("\t3.converse all star ราคา 2100 บาท")
    print("\t4.vans slip on ราคา 1990 บาท")
    print("\t5.vans old skool ราคา 2400 บาท")
def pickmenu():
	global pick
	print("\nรายการสินค้า\n 1.nike cortez\n 2.adidas superstar\n 3.converse all star\n 4.vans slip on\n 5. vans old skool")
	pick = int(input('เลือกหยิบสินค้าหมายเลข : '))
	if pick == 1:
		listshop[0] += 1
	elif pick == 2:
		listshop[1] += 1
	elif pick == 3:
		listshop[2] += 1
	elif pick == 4:
		listshop[3] += 1
	elif pick == 5:
		listshop[4] += 1

def allpick():
	list_sk = ["nike cortez" ,"adidas superstar" ,"converse all star" ,"vans slip on" ,"vans old skool"]
	list_cost = [2300,1400,2100,1990,2400]
	for i in range(5):
		print("{0:-<20}{1:-<10}{2}".format(list_sk[i],listshop[i],listshop[i]*list_cost[i]))

def outpick():
	print('รายการสินค้า\n 1.nike cortez\n 2.adidas superstar\n 3.converse all star\n 4.vans slip on\n 5.vans old skool')
	outpick = int(input("เลือกลำดับสินค้าที่จะหยิบออก หรือพิมพ์ -1 เพื่อออก"))
	if outpick == 1:
		listshop[0] -=1
	elif outpick == 2:
		listshop[1] -=1
	elif outpick == 3:
		listshop[2] -=1
	elif outpick == 4:
		listshop[3] -=1
	elif outpick == 5:
		listshop[4] -=1

while True:
	menu()
	if choice == '1':
		costmenu()
	elif choice == '2':
		pickmenu()
	elif choice == '3':
		allpick()
	elif choice == '4':
		outpick()
	elif choice == '5':
		ch = input("ต้องการใช้งานโปรแกรมต่อหรือไม่ y/n: ")
		if ch == 'y':
		   break
		elif ch == 'n':
		   continue