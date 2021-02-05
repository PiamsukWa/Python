"""
print("-"*50)
students_amount = int(input("Please enter amount of students : "))
print("-"*50)
students = [0 , 0 , 0 , 0 , 0 , 0]
score = [" 90-100 : "," 80-89  : "," 70-79  : "," 60-69  : ", " 50-59  : "," 0-49   : "]
n = 1
while n <= students_amount : 
    result = int(input("Please enter score of students  : "))
    if result <= 100 and result >=  90 :
        students [0] += 1 
    elif result <= 90 and result >= 80 :
        students [1] += 1
    elif result <= 80 and result >= 70 :
        students [2] += 1
    elif result <= 70 and result >= 60 :
        students [3] += 1
    elif result <= 60 and result >= 50 :
        students [4] += 1
    elif result <= 50 and result >=  0 :
        students [5] += 1
    n = n + 1 
for n in range(0,6) :
    print(score[n],"*"*students[n],) """

print("-"*50)
students_amount = int(input("Please enter amount of students : "))
print("-"*50)
students = [0 , 0 , 0 , 0 , 0 , 0]
score = [" 90-100 : "," 80-89  : "," 70-79  : "," 60-69  : ", " 50-59  : "," 0-49   : "]
for i in range(0,students_amount) :
    result = int(input("pls enter score of students : "))
    if result <= 100 and result >= 90 :
        students [0] += 1
    elif result <= 90 and result >= 80 :
        students [1] += 1
    elif result <= 80 and result >= 70 :
        students [2] += 1
    elif result <= 70 and result >= 60 :
        students [3] += 1
    elif result <= 60 and result >= 50 : 
        students [4] += 1
    elif result <= 50 and result >= 0 :
        students [5] += 1
for i in range(0,6) :
    print(score[i],students[i]*"*")