#แบบฝึกหัด 5.1
def add():
    global name,grade,sex,province,department
    print("-"*20+"แนะนำตัว"+"-"*20)
    add = input("ชื่อ-สกุล  :  ชั้น  :  เพศ  : จังหวัด : สาขา         ")  
    addnew = add.split(":")
    name = add[0]
    grade = add[1]
    sex = add[2]
    province = add[3]
    department = add[4]
class nisit :
    def __init__(self,name,grade,sex,province,department) :
        self.name = name
        self.grade = grade
        self.sex = sex
        self.province = province 
        self.department = department
    
    def showname(self) :
        print("สวัสดีค่ะ ฉันชื่อ"+self.name+"เรียนอยู่ชั้นปีที่" +self.grade+ "เพศ" +self.sex+ "มาจากจังหวัด" +self.province+ "เรียนอยู่สาขา" +self.department)
add()
X = nisit(name,grade,sex,province,department)
X.showname() 