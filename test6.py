"""
print("Day Converter Program")
number_of_day  =  int(input ('Input  number of Days --> '))
print(number_of_day,"Day --> Hour", 24*number_of_day,"Hours")
print(number_of_day,"Day --> Minutes", 60*24*number_of_day,"Minutes")
print(number_of_day,"Day --> Seconds", 60*60*24* number_of_day,"Seconds")
"""
"""
#list 
listfriend = ['Jan','Cream','Phu','Bam','Aom','Pee','Bas','Kong','Da','James']
listfriend[3] = "Boat"
listfriend[9] = "May"
print(listfriend[-1])
"""

"""
#list 
listfriend = ['Jan','Cream','Phu','Bam','Aom','Pee','Bas','Kong','Da','James']
listfriend.append("Dome")
listfriend.append("Poondang")
listfriend.insert(1,"Csa")
listfriend.insert(8,"Ped")
listfriend.remove("Aom")
listfriend.pop()
listfriend.pop(3)
del listfriend[7]
#listfriend.clear()
#del listfriend
print(listfriend) 
"""
"""
animal = {"cat","dog","rat","pig","ant"}
animal.add("monkey")
animal.update(["python","capibara","spider","wombat","penguin","crocodile"])
print(animal)
"""

print("โปรแกรมหยิบสินค้าใส่ตะกร้า")
listproducts = []
listproducts.append(input(" หยิบสินค้าชิ้นที่ 1 : ",))
listproducts.append(input(" หยิบสินค้าชิ้นที่ 2 : ",))
listproducts.append(input(" หยิบสินค้าชิ้นที่ 3 : ",))
listproducts.append(input(" หยิบสินค้าชิ้นที่ 4 : ",))
listproducts.append(input(" หยิบสินค้าชิ้นที่ 5 : ",))

print("\n สินค้าที่หยิบใส่ตะกร้า มีดังนี้")
print(" 1.",listproducts[0])
print(" 2.",listproducts[1])
print(" 3.",listproducts[2])
print(" 4.",listproducts[3])
print(" 5.",listproducts[4])

"""
print("โปรแกรมคำนวณค่าผ่านทางมอเตอร์เวย์")
print("-"*50)
print(" รกยนต์ 4 ล้อ กด 1 ")
print(" รถยนต์ 6 ล้อ กด 2 ")
print(" รถยนต์มากกว่า 6 ล้อ กด 3 \n")
car1_list = ["ลาดกระบัง-->บางบ่อ : 25 บาท","ลาดกระบัง-->บางประกง  : 30 บาท","ลาดกระบัง-->พนัสนิคม : 45 บาท","ลาดกระบัง-->บ้านบึง : 55 บาท","ลาดกระบัง-->บางพระ  : 60 บาท"]
car2_list = ["ลาดกระบัง-->บางบ่อ : 40 บาท","ลาดกระบัง-->บางประกง  : 45 บาท","ลาดกระบัง-->พนัสนิคม : 75 บาท","ลาดกระบัง-->บ้านบึง : 90 บาท","ลาดกระบัง-->บางพระ  : 100 บาท"]
car3_list = ["ลาดกระบัง-->บางบ่อ : 60 บาท","ลาดกระบัง-->บางประกง  : 70 บาท","ลาดกระบัง-->พนัสนิคม : 110 บาท","ลาดกระบัง-->บ้านบึง: 130 บาท","ลาดกระบัง-->บางพระ : 140 บาท"]
car = int(input("\n เลือกยานพาหนะ : "))
if car == 1 :
    print(" ค่าบริการรถยนต์ 4 ล้อ")
    for x in car1_list : 
        print("\n", x )
elif car == 2 :
    print(" ค่าบริการรถยนต์ 6 ล้อ")
    for x in car2_list : 
        print("\n", x )
elif car == 3 :
    print(" ค่าบริการรถยนต์ 6 ล้อขึ้นไป")
    for x in car3_list : 
        print("\n", x )
        """