#แบบฝึกหัดที่ 4.3
import time
name = []
score = []
temes = []
hlt = []
def time_():
    timeis = time.localtime()
    a = time.strftime('%d %B %Y, %H:%M:%S', timeis)
    print(a)

def input_():
    for i in range(num):
        print("ป้อนข้อมูลคนที่ ",1+i)
        na = input("ชื่อผู้ซ้อม : ")
        sc = float(input("คะแนน : "))
        t = float(input("ระยะเวลำที่ใช้ : "))
        name.append(na)
        score.append(sc)
        temes.append(t)
        hlt.append(sc/t)

'''def no_():
    for i in range(num):
        j = i
        for j in range(num):
            if hlt[i] > hlt[j]:
                a,b,c,d = hlt[i],name[i],score[i],temes[i]
                hlt[i],name[i],score[i],temes[i] = hlt[j],name[j],score[j],temes[j]
                hlt[j],name[j],score[j],temes[j] = a,b,c,d'''

def output_():
    print("-"*80)
    print("{0:-<6}{1:-<6}{2:-<8}{3:-<17}{4:-<12}{5:-<15}{6}".format("NO.","PTS","TIME","COMPETITOR#Name","HIT FACTOR","STATE POINTS","STATE PERCENT"))
    print("-"*80)
    for i in range(num):
        stawe_po = (hlt[i]/hlt[0])*50
        stawe_pe = (stawe_po/(hlt[0]/hlt[0]*50))*100
        print("{0: <6}{1: <6}{2: <8}{3: <17}{4: <12}{5: <15}{6}".format(i+1,int(score[i]),"%.2f"%temes[i],name[i],"%.4f"%hlt[i],"%.4f"%stawe_po,"%.2f"%stawe_pe))
    
num = int(input("พิมพ์จำนวนผู้ที่ซ้อมยิงปืน:"))
input_()
#no_()
timeis = time.localtime()
a = time.strftime('%A', timeis)
b = time.strftime('%Y', timeis)
print("Shotgun "+a+" Training",b,"\nCondtion : 1")
time_()
output_()