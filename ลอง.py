'''
p=["pom","พอม","แพม","สุด","หล่อ"]
for i in range(5):
    print("{0:-<15}".format(p[i]))
'''
"""
list_sk = ["nike cortez" ,"adidas superstar" ,"converse all star" ,"vans slip on" ,"vans old skool"]
list_cost = [2300,1400,2100,1990,2400]
for i in list_sk:
	print("{0:-<20}{1:-<10}".format(i,list_cost[int(i)]))

word = {
    "Bom" : "Pom,poo",
    "tity":"yu",
    "Plaiifah" : "Bam",
}
print(word["Bom"])"""

'''
B=int(input("กรุณาเพิ่มตัวเลข : "))
if B%2==0:
    print ("even")
else:
    print ("odd")
'''
class Car:
   car_list = []

   def __init__(self, make, model, price):
       self.make = make
       self.model = model
       self.price = price

       self.car_list.append(self)

#this is the part of the code that i'm stuck with

   def price_check(self):
       for i in Car.car_list:
           if New_Car.make == self.make:
               return i.price
        else:
            print("Not available")


 BMW = Car('BMW', '1 Series', "£20,000")
 Ferrari = Car('Ferrari', 'Italia', "£90,000")

New_Car = Car(
      input("What is make of your car? "), input("What is the model? "), "")

 print("The cost of this car is: ", New_Car.price_check())