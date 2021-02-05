'''import os
choice = 0
dictionary = {}

def menu() :
    global choice
    print ("พจนานุกรม\n 1.เพิ่มคำศัพท์\n 2.แสดงคำศัพท์\n 3.ลบคำศัพท์\n 4.ออกจากโปรแกรม\n")
    choice = input("กรุณาเลือกคำสั่ง : ")

def add_word() :
    word = input("เพิ่มคำศัพท์ : ")
    typ = input("ชนิดคำศัพท์ (n , v , adj , adv) : ")
    mean = input("ความหมาย : ")
    dictionary.update({word:{mean,typ}})
    print ("\n")

def show_word() :
    print ("คำศัพท์ของคุณมีดังต่อไปนี้\n คำศัพท์  {'ประเภท','ความหมาย'}")
    for k,v in dictionary.items() :
        print (k+"      ",v)

def remove_word() :
    remove = input ("พิมพ์คำศัพท์ที่ต้องการลบ : ")
    confirm = input ("คุณแน่ใจใช่ไหมว่าต้องการลบ (y/n) : ")
    if confirm == "y" :
        dictionary.pop(remove)
        print ("คุณได้ทำการลบ"+remove+"จาก Dictionary เรียบร้อยแล้ว")
    elif confirm == "n" :
        print ("คุณไม่ได้ลบคำศัพท์\n")

while True :
    menu()
    if choice == "1" :
        clearscreen = os.system("cls")
        add_word()
    elif choice == "2" :
        clearscreen = os.system("cls")
        show_word()
    elif choice == "3" :
        clearscreen = os.system("cls")
        remove_word()
    elif choice == "4" :
        a = input("คุณต้องการออกจากโปรแกรมใช่หรือไม่ ( y / n ) : ")
        if a.lower() == "n" :
            clearscreen = os.system("cls")
        elif a.lower() == "y" :
            clearscreen = os.system("cls")
            print ("คุณได้ออกจากโปรแกรม")
            break'''

#แบบฝึกหัดที่ 4.2
word = {}
def menu():
	print("-"*50)
	print("พจนานุกรม\n 1.เพิ่มคำศัพท์\n 2.แสดงคำศัพท์\n 3.ลบคำศัพท์\n 4.ออกจากโปรแกรม\n")
def add():
	w = input("เพิ่มคำศัพท์ : " )
	t = input("ชนิดคำศัพท์ (n,v,adj,adv) : ")
	m = input("ความหมาย : ")
	word[w]="{0: <15}{1: <15}".format(t,m)
def view():
	print("-"*50)
	print(" "*20 +"คำศัพท์ของคุณมีดังนี้"+"	"*20)
	print("-"*50)
	print("{0:-<15}{1:-<15}{2:-<10}".format("คำศัพท์" , "ประเภท", "ความหมาย"))
	for i in word:
		print("{0: <15}{1: <15}".format(i,word[i]))
def remove():
	x = input("พิมพ์คำศัพท์ที่ต้องการลบ :")
	z = input("คุณแน่ใจใช่ไหมว่าต้องการลบ (y/n) :")
	if z == "y":
		word.pop(x)
	else:
		print(" ")

while True:
	menu()
	me = int(input("เลือกรายการที่ต้องการ : "))
	if me == 1:
		add()
	elif me == 2:
		view()
	elif me == 3:
		remove()
	else:
		z = input("คุณแน่ใจใช่มั้ยว่าต้องการออกจากโปรแกรม (y or n): ")
		if z == "y":
			break
		else:
			print(" ")