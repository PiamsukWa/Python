#แบบฝึกหัด 5.1
def add():
    global name,grade,sex,province,department,faculty
    print(""*20+"แนะนำตัว"+""*20)

    add = input("ชื่อ-สกุล :  ชั้น  :  เพศ  :  จังหวัด  :  สาขา  :  คณะ         ")  
    addnew = add.split(":")
    name = addnew[0]
    grade = addnew[1]
    sex = addnew[2]
    province = addnew[3]
    department = addnew[4]
    faculty = addnew[5]
class nisit :
    def __init__(self,name,grade,sex,province,department,faculty) :
        self.name = name
        self.grade = grade
        self.sex = sex
        self.province = province 
        self.department = department
        self.faculty = faculty

    def showname(self) :
        print("สวัสดีค่ะ ฉันชื่อ    "+self.name+  "     เรียนอยู่ชั้นปีที่    "  +self.grade+  "     เพศ     "   +self.sex+  "    มาจากจังหวัด    "   +self.province+  "     เรียนอยู่สาขา   "   +self.department+   "     เรียนอยู่คณะ       "  +self.faculty)
add()
X = nisit(name,grade,sex,province,department,faculty)
X.showname()