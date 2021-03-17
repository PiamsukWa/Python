from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3 as db
import sqlite3
moneytype =[1000, 500, 100, 50, 20, 10, 5, 2, 1]
amount_money = [0, 0, 0, 0, 0]
money_type = [10, 5, 1, 2,]

windows = Tk()
windows.option_add("*Font", " JasmineUPC 25")
windows.title("ตู้กดสินค้าและแลกเหรียญ P&B")
windows.minsize (width=1280 , height=720)

def head():
    Label(windows, text = "ยินดีต้อนรับ",fg="#FFFFFF" ,bg="#006699",width=73, height=2 ).pack() #Lable -> widget
    #tk.Label (windows , text="กรุณาเลือกรายการ",width=73, height=1 , bg="#F0F8FF").pack()
    
def home():
    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
    win_screen.place(relx=0.5, rely=0.27, relwidth=1.2, relheight=0.8, anchor='n')

    frame = tk.Frame(windows, bg='#4682B4',)
    frame.place(relx = 0.5, rely=0.35, relwidth=0.57, relheight=0.4, anchor='n')
    Button(windows, text = "สำหรับผู้ซื้อ 🛒",fg="#000000" ,bg="#FFE4E1", width = 25 ,command=customer).place(relx=0.5, rely=0.45, relwidth=0.4, relheight=0.1, anchor='n')
    Button(windows, text = "สำหรับผู้ขาย 💰 ",fg="#000000" ,bg="#FFFACD", width = 25, command= create_).place(relx=0.5, rely=0.57, relwidth=0.4, relheight=0.1, anchor='n')
    
    creator = tk.Frame(windows, bg='#006699', bd=6) #กรอบข้อความ
    creator.place(relx=0.5, rely=0.8, relwidth=0.57, relheight=0.18, anchor='n')

    tb = Label (creator, text="จัดทำโดย\n1. นางสาวเปี่ยมสุข วาทิรอยรัมย์\tรหัสนักศึกษา 633050133-0\n2. นางสาวพิรญา  ศรีพิมพ์\tรหัสนักศึกษา 633050425-7",bg="#F0F8FF",fg="#000000",bd=1)
    tb.place(relwidth=1, relheight=1)

def create_():
    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
    win_screen.place(relx=0.5, rely=0.31, relwidth=0.58, relheight=0.8, anchor='n')

    def login():
        frame = tk.Frame(windows, bg='#E6E6FA',bd=5 )
        frame.place(relx = 0.5, rely=0.35, relwidth=0.57, relheight=0.40, anchor='n')
        
        box = Label (frame, text="กรุณากรอกรหัสผ่าน", bg = "#FFFACD")
        box.place(relx=0.5, rely=0.09, relwidth=0.6, relheight=0.2, anchor='n')

        boxpass = tk.Entry(frame, show = '❤', fg="#CC0033")
        boxpass.place(relx=0.5, rely=0.37, relwidth=0.6, relheight=0.2, anchor='n')
        
        def checkpwd() :
            password = str(boxpass.get())
            if password=='123456' :
                def creator_menu():
                    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
                    win_screen.place(relx=0.5, rely=0.31, relwidth=0.58, relheight=0.68, anchor='n')

                    frame = tk.Frame(windows, bg='#E6E6FA',)
                    frame.place(relx = 0.5, rely=0.35, relwidth=0.57, relheight=0.39, anchor='n')
                    Button(windows, text = "🛒 เพิ่มสินค้า",fg="#000000" ,bg="#FFDEAD", width = 25,command=insertpro).place(relx=0.5, rely=0.37, relwidth=0.2, relheight=0.08, anchor='n')
                    Button(windows, text = "📜 แสดงสินค้า",fg="#000000" ,bg="#FFFACD", width = 25,command=showpro).place(relx=0.5, rely=0.46, relwidth=0.2, relheight=0.08, anchor='n')
                    Button(windows, text = "🔄 แก้ไขสินค้า",fg="#000000" ,bg="#FFE4E1", width = 25,command=updatepro).place(relx=0.5, rely=0.55, relwidth=0.2, relheight=0.08, anchor='n')
                    Button(windows, text = "❌ ลบสินค้า",fg="#000000" ,bg="#FFA07A", width = 25,command=deletepro).place(relx=0.5, rely=0.64, relwidth=0.2, relheight=0.08, anchor='n')
                    
                    button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=home)
                    button2.place(relx=0.50, rely=0.8, relwidth=0.19, relheight=0.08,anchor='n')

                    creator = tk.Frame(windows, bg='#006699', bd=6) 
                    creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง
                    
                creator_menu()

            else :
                win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
                win_screen.place(relx=0.5, rely=0.31, relwidth=0.58, relheight=0.68, anchor='n')

                frame = tk.Frame(windows, bg='#f0f0f0', bd=6)
                frame.place(relx=0.5, rely=0.4, relwidth=0.6, relheight=0.07, anchor='n')
                
                nameblock = Label (frame, text="รหัสผ่านไม่ถูกต้อง",bg= '#f0f0f0')
                nameblock.place(relwidth=1, relheight=1)


                button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#FFDEAD",fg='#000000',command=home)
                button2.place(relx=0.40, rely=0.81, relwidth=0.19, relheight=0.08,anchor='n')

                button3 = tk.Button(windows,text='กรอกรหัสผ่านอีกครั้ง',bg="#FFB6C1",fg='#000000',command=create_)
                button3.place(relx=0.60, rely=0.81, relwidth=0.19, relheight=0.08,anchor='n')

                creator = tk.Frame(windows, bg='#006699', bd=6) 
                creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n')
                

        button1 = tk.Button(windows,text='เข้าสู่ระบบ',bg="#2E8B57",fg='#FFFFFF',command=checkpwd)
        button1.place(relx=0.44, rely=0.60, relwidth=0.1, relheight=0.1, anchor='n')

        button2 = tk.Button(windows,text='ยกเลิก',bg="#CD5C5C",fg='#FFFFFF',command=home)
        button2.place(relx=0.56, rely=0.60, relwidth=0.1, relheight=0.1,anchor='n')

        creator = tk.Frame(windows, bg='#006699', bd=6) 
        creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง

    login()

def insertpro():
    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
    win_screen.place(relx=0.5, rely=0.31, relwidth=0.58, relheight=0.68, anchor='n')

    frame = tk.Frame(windows, bg='#E6E6FA')
    frame.place(relx = 0.5, rely=0.38, relwidth=0.57, relheight=0.35, anchor='n')
    tk.Label(windows , text="กรุณาป้อนข้อมูลสินค้า").place(relx=0.5, rely=0.31, relwidth=0.25, anchor='n')

    """def data():
            conn = sqlite3.connect("Databaseexample.db")
            c = conn.cursor()
            c.execute('CREATE TABLE IF NOT EXISTS users (ID integer PRIMARY KEY AUTOINCREMENT , Products TEXT, Price TEXT, amount TEXT NOT NULL)')
            conn.commit()
            conn.close()
    data()"""

    def savedata():
        conn = sqlite3.connect("Databaseexample.db")
        c = conn.cursor()
        c.execute('INSERT INTO users(Products, Price, amount) VALUES(?,?,?)',(box2.get(),box3.get(),box4.get()))
        conn.commit()
        text=('บันทึกข้อมูลเรียบร้อยค่ะ')
        messagebox.showinfo(message=text)
        print('save') 

    box = Label(frame, text="ชื่อสินค้า", bg='#FFFACD')
    box.place(relx=0.19, rely=0.28, relwidth=0.3, relheight=0.15, anchor='n')
    box2 = StringVar()
    box2 = tk.Entry(frame, textvariable = box2)
    box2.place(relx=0.66, rely=0.28, relwidth=0.6, relheight=0.15, anchor='n')
    box2.focus()

    box = Label(frame, text="ราคา", bg='#FFFACD')
    box.place(relx=0.19, rely=0.47, relwidth=0.3, relheight=0.15, anchor='n')
    box3 = StringVar()
    box3 = tk.Entry(frame, textvariable = box3)
    box3.place(relx=0.66, rely=0.47, relwidth=0.6, relheight=0.15, anchor='n')

    box = Label(frame, text="จำนวน", bg='#FFFACD')
    box.place(relx=0.19, rely=0.66, relwidth=0.3, relheight=0.15, anchor='n')
    box4 = StringVar()
    box4 = tk.Entry(frame, textvariable = box4)
    box4.place(relx=0.66, rely=0.66, relwidth=0.6, relheight=0.15, anchor='n')

    
    button1 = tk.Button(windows,text='บันทึก',bg="#2E8B57",fg='#FFFFFF',command = savedata) #ดึงชื่อสินค้าจาก database มาลบ
    button1.place(relx=0.38, rely=0.82, relwidth=0.125, relheight=0.07, anchor='n')

    button2 = tk.Button(windows,text='ยกเลิก',bg="#CD5C5C",fg='#FFFFFF',command=home)
    button2.place(relx=0.509, rely=0.82, relwidth=0.125, relheight=0.07,anchor='n')

    button3 = tk.Button(windows,text='ดูข้อมูลสินค้า',bg="#1E90FF",fg='#FFFFFF',command= showpro)
    button3.place(relx=0.64, rely=0.82, relwidth=0.125, relheight=0.07,anchor='n')
    
    creator = tk.Frame(windows, bg='#006699', bd=6) #กรอบข้อความ
    creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n')
    
def showpro():
    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
    win_screen.place(relx=0.5, rely=0.31, relwidth=0.58, relheight=0.68, anchor='n')

    frame = tk.Frame(windows, bg='#E6E6FA')
    frame.place(relx = 0.5, rely=0.38, relwidth=0.57, relheight=0.35, anchor='n')
    tk.Label(windows , text="ข้อมูลสินค้า").place(relx=0.5, rely=0.31, relwidth=0.25, anchor='n')

    conn = sqlite3.connect("Databaseexample.db")
    c = conn.cursor()
    row = c.execute('SELECT * FROM users ')
    total = c.rowcount
    conn.commit()

    tv = ttk.Treeview(frame, columns=(1,2,3,4), show='headings')
    tv.pack(padx=40,pady=30)

    style = ttk.Style()
    style.configure("Treeview", font=('EucrosiaUPC', 18)) # Modify the font of the body
    style.configure("Treeview.Heading", font=('EucrosiaUPC', 20 ,'bold')) # Modify the font of the headings

    tv.heading(1, text = 'ID')
    tv.heading(2, text = 'Products')
    tv.heading(3, text = 'Price')
    tv.heading(4, text = 'amount')

    for i in row:
        tv.insert('','end',values=i)
    
    button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=home)
    button2.place(relx=0.5, rely=0.81, relwidth=0.19, relheight=0.08,anchor='n')

    creator = tk.Frame(windows, bg='#006699', bd=6) #กรอบข้อความ
    creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n')

def updatepro():
    global boxID
    global boxpro
    global boxprice
    global boxam

    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
    win_screen.place(relx=0.5, rely=0.31, relwidth=0.58, relheight=0.68, anchor='n')

    frame = tk.Frame(windows, bg='#E6E6FA')
    frame.place(relx = 0.5, rely=0.38, relwidth=0.57, relheight=0.35, anchor='n')
    
    tk.Label(windows , text="กรุณาแก้ไขสินค้า").place(relx=0.5, rely=0.31, relwidth=0.25, anchor='n')
    
    box = Label(frame, text="ID", bg='#FFFACD')
    box.place(relx=0.19, rely=0.09, relwidth=0.3, relheight=0.15, anchor='n')
    
    boxID = tk.Entry(frame, textvariable = boxID)
    boxID.place(relx=0.66, rely=0.09, relwidth=0.6, relheight=0.15, anchor='n')

    box = Label(frame, text="ชื่อสินค้า", bg='#FFFACD')
    box.place(relx=0.19, rely=0.28, relwidth=0.3, relheight=0.15, anchor='n')

    boxpro = tk.Entry(frame, textvariable = boxpro)
    boxpro.place(relx=0.66, rely=0.28, relwidth=0.6, relheight=0.15, anchor='n')
    boxpro.focus()

    box = Label(frame, text="ราคา", bg='#FFFACD')
    box.place(relx=0.19, rely=0.47, relwidth=0.3, relheight=0.15, anchor='n')

    boxprice = tk.Entry(frame, textvariable = boxprice)
    boxprice.place(relx=0.66, rely=0.47, relwidth=0.6, relheight=0.15, anchor='n')

    box = Label(frame, text="จำนวน", bg='#FFFACD')
    box.place(relx=0.19, rely=0.66, relwidth=0.3, relheight=0.15, anchor='n')

    boxam = tk.Entry(frame, textvariable = boxam)
    boxam.place(relx=0.66, rely=0.66, relwidth=0.6, relheight=0.15, anchor='n')

    button1 = tk.Button(windows,text='บันทึก',bg="#2E8B57",fg='#FFFFFF',command = edit) #ดึงชื่อสินค้าจาก database มาลบ
    button1.place(relx=0.38, rely=0.82, relwidth=0.125, relheight=0.07, anchor='n')

    button2 = tk.Button(windows,text='ยกเลิก',bg="#CD5C5C",fg='#FFFFFF',command=home)
    button2.place(relx=0.509, rely=0.82, relwidth=0.125, relheight=0.07,anchor='n')

    button3 = tk.Button(windows,text='ดูข้อมูลสินค้า',bg="#1E90FF",fg='#FFFFFF',command= showpro)
    button3.place(relx=0.64, rely=0.82, relwidth=0.125, relheight=0.07,anchor='n')
    
    creator = tk.Frame(windows, bg='#006699', bd=6) #กรอบข้อความ
    creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n')

def edit():
    num1 = str(boxID.get())
    prod1 = str(boxpro.get())
    pric1 = str(boxprice.get())
    amou1 = str(boxam.get())
    text=('อัปเดตข้อมูลเรียบร้อยค่ะ')
    messagebox.showinfo(message=text)

    conn = sqlite3.connect('Databaseexample.db')
    c = conn.cursor()
    #data = (num1,pric1,amou1,prod1)
    sql = 'UPDATE users SET Products = "{}", price = "{}", amount = "{}" WHERE ID = "{}"'.format(prod1,pric1,amou1,num1)
    print(sql)
    c.execute(sql)
    conn.commit() 
    conn.close()
    print('Upadate Success')

def deletepro():
    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
    win_screen.place(relx=0.5, rely=0.31, relwidth=0.58, relheight=0.68, anchor='n')

    frame = tk.Frame(windows, bg='#E6E6FA')
    frame.place(relx = 0.5, rely=0.38, relwidth=0.57, relheight=0.4, anchor='n')
    
    tk.Label(windows , text="กรุณาป้อนชื่อสินค้าที่ต้องการลบ").place(relx=0.5, rely=0.31, relwidth=0.25, anchor='n')

    conn = sqlite3.connect("Databaseexample.db")
    c = conn.cursor()
    row = c.execute('SELECT * FROM users ')
    total = c.rowcount
    #print('total Data Entries : '+str(total))
    conn.commit()

    tv = ttk.Treeview(frame, columns=(1,2,3,4), show='headings')
    tv.pack(padx=40,pady=30)

    style = ttk.Style()
    style.configure("Treeview", font=('JasmineUPC', 18)) # Modify the font of the body
    style.configure("Treeview.Heading", font=('JasmineUPC', 20 ,'bold')) # Modify the font of the headings

    tv.heading(1, text = 'ID')
    tv.heading(2, text = 'Products')
    tv.heading(3, text = 'Price')
    tv.heading(4, text = 'amount')

    for i in row:
        tv.insert('','end',values=i)

    def deleteprodata(): #ได้ซักที ขอบคุณ stackoverflow.com ค่ะ
        data = boxID.get()
        conn = sqlite3.connect('Databaseexample.db')
        c = conn.cursor()
        c.execute('DELETE FROM users WHERE ID = ?  ' ,[data])
        conn.commit() 
        conn.close()
        text=('ลบข้อมูลเรียบร้อยค่ะ')
        messagebox.showinfo(message=text)
        print('Delete Success')

    box = Label(frame, text="ID", bg='#FFFACD')
    box.place(relx=0.19, rely=0.85, relwidth=0.3, relheight=0.1, anchor='n')
    
    boxID = StringVar()
    boxID = tk.Entry(frame, textvariable = boxID)
    boxID.place(relx=0.66, rely=0.85, relwidth=0.6, relheight=0.1, anchor='n')

    button1 = tk.Button(windows,text='ยืนยัน',bg="#2E8B57",fg='#FFFFFF',command = deleteprodata) #ดึงชื่อสินค้าจาก database มาลบ
    button1.place(relx=0.38, rely=0.82, relwidth=0.125, relheight=0.07, anchor='n')

    button2 = tk.Button(windows,text='ยกเลิก',bg="#CD5C5C",fg='#FFFFFF',command=home)
    button2.place(relx=0.509, rely=0.82, relwidth=0.125, relheight=0.07,anchor='n')

    button3 = tk.Button(windows,text='ดูข้อมูลสินค้า',bg="#1E90FF",fg='#FFFFFF',command= showpro)
    button3.place(relx=0.64, rely=0.82, relwidth=0.125, relheight=0.07,anchor='n')
    
    creator = tk.Frame(windows, bg='#006699', bd=6) #กรอบข้อความ
    creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n')

def customer():
    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
    win_screen.place(relx=0.5, rely=0.31, relwidth=0.58, relheight=0.68, anchor='n')

    frame = tk.Frame(windows, bg='#E6E6FA')
    frame.place(relx = 0.5, rely=0.38, relwidth=0.57, relheight=0.35, anchor='n')
    Button(windows, text = "กดสินค้า 🍬",fg="#000000" ,bg="#BEBEBE", width = 25,command= sell ).place(relx=0.5, rely=0.45, relwidth=0.4, relheight=0.1, anchor='n')
    Button(windows, text = "แลกเงิน 💵",fg="#000000" ,bg="#FFDAB9", width = 25,command =chang).place(relx=0.5, rely=0.57, relwidth=0.4, relheight=0.1, anchor='n')

    button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=home)
    button2.place(relx=0.50, rely=0.8, relwidth=0.19, relheight=0.08,anchor='n')

    creator = tk.Frame(windows, bg='#006699', bd=6) 
    creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง

def sell(): 
    
    savetotal[0] = 0
    changmoney.clear()
    Frame(windows, bg= '#f0f0f0', bd=5).place(relx=0.5, rely=0.35, relwidth=0.70, relheight=0.68, anchor='n')
    
    button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=home)
    button2.place(relx=0.50, rely=0.83, relwidth=0.19, relheight=0.06,anchor='n')

    creator = tk.Frame(windows, bg='#006699', bd=6)     
    creator.place(relx=0.50, rely=0.92, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง

    block = Frame(windows)
    block.place(relx=0.5,rely=0.3, relwidth=0.7, relheight=0.5, anchor='n')

    Button(block, text = "กาแฟ 15 บาท",fg="#000000" ,bg="#99FFFF", width = 13,bd=9,command=coffee).place(relx=0.2, rely=0.3, relwidth=0.25, relheight=0.15, anchor='n')
    Button(block, text = "โออิชิ 20 บาท",fg="#000000" ,bg="#87CEEB", width = 13,bd=9,command=Oichi).place(relx=0.51, rely=0.3, relwidth=0.25, relheight=0.15, anchor='n')
    Button(block, text = "สปอนเซอร์ 12 บาท",fg="#000000" ,bg="#99FF99", width = 13,bd=9,command=Sponser).place(relx=0.81, rely=0.3, relwidth=0.25, relheight=0.15, anchor='n')
    Button(block, text = "มาม่าต้มยำบิ๊ก 10 บาท",fg="#000000" ,bg="#BDB76B", width = 13,bd=9,command=big).place(relx=0.2, rely=0.8, relwidth=0.25, relheight=0.15, anchor='n')
    Button(block, text = "มาม่าเย็นตาโฟ 10 บาท",fg="#000000" ,bg="#EEE8AA", width = 13,bd=9,command=fo).place(relx=0.51, rely=0.8, relwidth=0.25, relheight=0.15, anchor='n')
    Button(block, text = "มาม่าหมูต้มยำ 10 บาท",fg="#000000" ,bg="#F4A460", width = 13,bd=9,command=pig).place(relx=0.81, rely=0.8, relwidth=0.25, relheight=0.15, anchor='n')

    photo00 = PhotoImage(file="coffee.png")   
    Label(windows, image = photo00).place(relx=0.28,rely=0.32,anchor='n')

    photo01 = PhotoImage(file="Oichi.png")
    Label(windows, image=photo01).place(relx=0.50,rely=0.28,anchor='n')

    photo02 = PhotoImage(file="Sponser.png")
    Label(windows, image=photo02).place(relx=0.70,rely=0.28,anchor='n')

    photo03 = PhotoImage(file="มาม่าต้มยำบิ๊ก.png")
    Label(windows, image=photo03).place(relx=0.29,rely=0.53,anchor='n')

    photo04 = PhotoImage(file="มาม่าเย็นตาโฟ.png")
    Label(windows, image=photo04).place(relx=0.50,rely=0.54,anchor='n')
 
    photo05 = PhotoImage(file="มาม่าหมูต้มยำ.png")
    Label(windows, image=photo05).place(relx=0.70,rely=0.54,anchor='n')

    creator = tk.Frame(windows, bg='#006699', bd=6) #กรอบข้อความ
    creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n')
    block.mainloop()

def coffee():
    
    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
    win_screen.place(relx=0.5, rely=0.27, relwidth=1.2, relheight=0.8, anchor='n')
    
    Name_Pro = str("กาแฟ")
    conn = sqlite3.connect("Databaseexample.db")
    c = conn.cursor()
    sql = 'SELECT * FROM users WHERE Products = "{}"'.format(Name_Pro)
    c.execute(sql)
    dataoutput = c.fetchall()
    for n in dataoutput :
        if Name_Pro == n[1] :
            Name = str(n[1])
            Price = str(n[2])
            Amount = str(n[3])
            Text = ("รายการ : "+Name+"\nราคา : "+Price+"\nจำนวนคงเหลือ : "+Amount)
            changmoney.append(Price)
            changmoney.append(Amount)
            changmoney.append(Name_Pro)
            #print (changmoney)
            #print (Text)
    
    if(int(Amount) == 0):
        messagebox.showinfo(title="การแจ้งเตือน",message="ขออภัยค่ะ สินค้าหมด")
        sell()
    else:
        Label(windows,text=Text,fg="#000033",bg="#E6E6FA").place(relx=0.5, rely=0.3, relwidth=0.4, relheight=0.3, anchor='n')

        Button (windows, text = "ยกเลิก",fg="#000000" ,bg="#708090", width = 10,command=sell ).place(relx=0.25, rely=0.70, relwidth=0.1, relheight=0.1, anchor='n')
        Button (windows, text = "ยืนยัน",fg="#000000" ,bg="#E9967A", width = 10,command=ok).place(relx=0.75, rely=0.70, relwidth=0.1, relheight=0.1, anchor='n')

        button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=home)
        button2.place(relx=0.50, rely=0.8, relwidth=0.19, relheight=0.08,anchor='n')

        creator = tk.Frame(windows, bg='#006699', bd=6) 
        creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง  

    

def Oichi():  
    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
    win_screen.place(relx=0.5, rely=0.27, relwidth=1.2, relheight=0.8, anchor='n')

    Name_Pro = str("โออิชิ")
    conn = sqlite3.connect("Databaseexample.db")
    c = conn.cursor()
    sql = 'SELECT * FROM users WHERE Products = "{}"'.format(Name_Pro)
    c.execute(sql)
    dataoutput = c.fetchall()
    for n in dataoutput :
        if Name_Pro == n[1] :
            Name = str(n[1])
            Price = str(n[2])
            Amount = str(n[3])
            Text = ("รายการ : "+Name+"\nราคา : "+Price+"\nจำนวนคงเหลือ : "+Amount)
            #print (Text)
            changmoney.append(Price)
            changmoney.append(Amount)
            changmoney.append(Name_Pro)

    if(int(Amount) == 0):
        messagebox.showinfo(title="การแจ้งเตือน",message="ขออภัยค่ะ สินค้าหมด")
        sell()
    else:
    
        Label(windows,text=Text,fg="#000033",bg="#E6E6FA").place(relx=0.5, rely=0.3, relwidth=0.4, relheight=0.3, anchor='n')

        
        Button(windows, text = "ยกเลิก",fg="#000000" ,bg="#708090", width = 10,command=sell ).place(relx=0.25, rely=0.70, relwidth=0.1, relheight=0.1, anchor='n')
        Button(windows, text = "ยืนยัน",fg="#000000" ,bg="#E9967A", width = 10,command=ok1).place(relx=0.75, rely=0.70, relwidth=0.1, relheight=0.1, anchor='n')

        
        button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=home)
        button2.place(relx=0.50, rely=0.8, relwidth=0.19, relheight=0.08,anchor='n')

        creator = tk.Frame(windows, bg='#006699', bd=6) 
        creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง

def Sponser():
    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
    win_screen.place(relx=0.5, rely=0.27, relwidth=1.2, relheight=0.8, anchor='n')

    Name_Pro = str("สปอนเซอร์")
    conn = sqlite3.connect("Databaseexample.db")
    c = conn.cursor()
    sql = 'SELECT * FROM users WHERE Products = "{}"'.format(Name_Pro)
    c.execute(sql)
    dataoutput = c.fetchall()
    for n in dataoutput :
        if Name_Pro == n[1] :
            Name = str(n[1])
            Price = str(n[2])
            Amount = str(n[3])
            Text = ("รายการ : "+Name+"\nราคา : "+Price+"\nจำนวนคงเหลือ : "+Amount)
            #print (Text)
            changmoney.append(Price)
            changmoney.append(Amount)
            changmoney.append(Name_Pro)

    if(int(Amount) == 0):
        messagebox.showinfo(title="การแจ้งเตือน",message="ขออภัยค่ะ สินค้าหมด")
        sell()
    else:

        Label(windows,text=Text,fg="#000033",bg="#E6E6FA").place(relx=0.5, rely=0.3, relwidth=0.4, relheight=0.3, anchor='n')

        Button(windows, text = "ยกเลิก",fg="#000000" ,bg="#708090", width = 10,command=sell ).place(relx=0.25, rely=0.70, relwidth=0.1, relheight=0.1, anchor='n')
        Button(windows, text = "ยืนยัน",fg="#000000" ,bg="#E9967A", width = 10,command=ok2).place(relx=0.75, rely=0.70, relwidth=0.1, relheight=0.1, anchor='n')

        button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=home)
        button2.place(relx=0.50, rely=0.8, relwidth=0.19, relheight=0.08,anchor='n')

        creator = tk.Frame(windows, bg='#006699', bd=6) 
        creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง
    
def big():
    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
    win_screen.place(relx=0.5, rely=0.27, relwidth=1.2, relheight=0.8, anchor='n')

    Name_Pro = str("มาม่าบิ๊กต้มยำ")
    conn = sqlite3.connect("Databaseexample.db")
    c = conn.cursor()
    sql = 'SELECT * FROM users WHERE Products = "{}"'.format(Name_Pro)
    c.execute(sql)
    dataoutput = c.fetchall()
    for n in dataoutput :
        if Name_Pro == n[1] :
            Name = str(n[1])
            Price = str(n[2])
            Amount = str(n[3])
            Text = ("รายการ : "+Name+"\nราคา : "+Price+"\nจำนวนคงเหลือ : "+Amount)
            #print (Text)
            changmoney.append(Price)
            changmoney.append(Amount)
            changmoney.append(Name_Pro)

    if(int(Amount) == 0):
        messagebox.showinfo(title="การแจ้งเตือน",message="ขออภัยค่ะ สินค้าหมด")
        sell()
    else:

    
        Label(windows,text=Text,fg="#000033",bg="#E6E6FA").place(relx=0.5, rely=0.3, relwidth=0.4, relheight=0.3, anchor='n')

        
        Button(windows, text = "ยกเลิก",fg="#000000" ,bg="#708090", width = 10,command=sell ).place(relx=0.25, rely=0.70, relwidth=0.1, relheight=0.1, anchor='n')
        Button(windows, text = "ยืนยัน",fg="#000000" ,bg="#E9967A", width = 10,command=ok3).place(relx=0.75, rely=0.70, relwidth=0.1, relheight=0.1, anchor='n')
        
        button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=home)
        button2.place(relx=0.50, rely=0.8, relwidth=0.19, relheight=0.08,anchor='n')

        creator = tk.Frame(windows, bg='#006699', bd=6) 
        creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง

def fo():
    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
    win_screen.place(relx=0.5, rely=0.27, relwidth=1.2, relheight=0.8, anchor='n')

    Name_Pro = str("มาม่าเย็นตาโฟ")
    conn = sqlite3.connect("Databaseexample.db")
    c = conn.cursor()
    sql = 'SELECT * FROM users WHERE Products = "{}"'.format(Name_Pro)
    c.execute(sql)
    dataoutput = c.fetchall()
    for n in dataoutput :
        if Name_Pro == n[1] :
            Name = str(n[1])
            Price = str(n[2])
            Amount = str(n[3])
            Text = ("รายการ : "+Name+"\nราคา : "+Price+"\nจำนวนคงเหลือ : "+Amount)
            #print (Text)
            changmoney.append(Price)
            changmoney.append(Amount)
            changmoney.append(Name_Pro)
    if(int(Amount) == 0):
        messagebox.showinfo(title="การแจ้งเตือน",message="ขออภัยค่ะ สินค้าหมด")
        sell()
    else:

        Label(windows,text=Text,fg="#000033",bg="#E6E6FA").place(relx=0.5, rely=0.3, relwidth=0.4, relheight=0.3, anchor='n')

        
        Button(windows, text = "ยกเลิก",fg="#000000" ,bg="#708090", width = 10,command=sell ).place(relx=0.25, rely=0.70, relwidth=0.1, relheight=0.1, anchor='n')
        Button(windows, text = "ยืนยัน",fg="#000000" ,bg="#E9967A", width = 10,command=ok4).place(relx=0.75, rely=0.70, relwidth=0.1, relheight=0.1, anchor='n')

        
        button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=home)
        button2.place(relx=0.50, rely=0.8, relwidth=0.19, relheight=0.08,anchor='n')

        creator = tk.Frame(windows, bg='#006699', bd=6) 
        creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง

def pig():
    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
    win_screen.place(relx=0.5, rely=0.27, relwidth=1.2, relheight=0.8, anchor='n')

    Name_Pro = str("มาม่าหมูต้มยำ")
    conn = sqlite3.connect("Databaseexample.db")
    c = conn.cursor()
    sql = 'SELECT * FROM users WHERE Products = "{}"'.format(Name_Pro)
    c.execute(sql)
    dataoutput = c.fetchall()
    for n in dataoutput :
        if Name_Pro == n[1] :
            Name = str(n[1])
            Price = str(n[2])
            Amount = str(n[3])
            Text = ("รายการ : "+Name+"\nราคา : "+Price+"\nจำนวนคงเหลือ : "+Amount)
            #print (Text)
            changmoney.append(Price)
            changmoney.append(Amount)
            changmoney.append(Name_Pro)
    if(int(Amount) == 0):
        messagebox.showinfo(title="การแจ้งเตือน",message="ขออภัยค่ะ สินค้าหมด")
        sell()
    else:

        Label(windows,text=Text,fg="#000033",bg="#E6E6FA").place(relx=0.5, rely=0.3, relwidth=0.4, relheight=0.3, anchor='n')

        Button(windows, text = "ยกเลิก",fg="#000000" ,bg="#708090", width = 10,command=sell ).place(relx=0.25, rely=0.70, relwidth=0.1, relheight=0.1, anchor='n')
        Button(windows, text = "ยืนยัน",fg="#000000" ,bg="#E9967A", width = 10,command=ok5).place(relx=0.75, rely=0.70, relwidth=0.1, relheight=0.1, anchor='n')
        
        button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=home)
        button2.place(relx=0.50, rely=0.8, relwidth=0.19, relheight=0.08,anchor='n')

        creator = tk.Frame(windows, bg='#006699', bd=6) 
        creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง

def ok():
    tv_total.set(f'เงินที่ได้รับ = 0')
    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
    win_screen.place(relx=0.5, rely=0.27, relwidth=1.2, relheight=0.8, anchor='n')
    Label(windows,text="กรุณาชำระเงิน").place(relx=0.5, rely=0.27, relwidth=0.2, relheight=0.1, anchor='n')
    Name_Pro = str("กาแฟ")
    conn = sqlite3.connect("Databaseexample.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM users''')
    dataoutput = c.fetchall()
    for n in dataoutput :
        if Name_Pro == n[1] :
            Name = str(n[1])
            Price = str(n[2])
            Amount = str(n[3])
            Text = ("รายการ : "+Name+"\nราคา : "+Price+"\nจำนวนคงเหลือ : "+Amount)
            #print (Text)

    Label(windows,text=Text,fg="#000033",bg="#FAEBD7").place(relx=0.25, rely=0.35, relwidth=0.2, relheight=0.4, anchor='n')
    frame = tk.Frame(windows, bg='#FAFAD2',)
    frame.place(relx = 0.6, rely=0.35, relwidth=0.5, relheight=0.4, anchor='n')

    def one_click():
        one = 1
        savetotal[0] += 1
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def five_click():
        five = 5
        savetotal[0] += 5
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def ten_click():
        ten = 10
        savetotal[0] += 10
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def twen_click():
        twen = 20
        savetotal[0] += 20
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def fif_click():
        fif = 50
        savetotal[0] += 50
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def onehun_click():
        onehun = 100
        savetotal[0] += 100
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    Button(windows, text = "1 บาท",fg="#000000" ,bg="#FFD700", width = 10,command = one_click).place(relx=0.45, rely=0.40, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "5 บาท",fg="#000000" ,bg="#98FB98", width = 10,command = five_click).place(relx=0.60, rely=0.40, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "10 บาท",fg="#000000" ,bg="#66CDAA", width = 10,command = ten_click).place(relx=0.75, rely=0.40, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "20 บาท",fg="#000000" ,bg="#FFA07A", width = 10 ,command = twen_click).place(relx=0.45, rely=0.55, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "50 บาท",fg="#000000" ,bg="#9932CC", width = 10,command = fif_click).place(relx=0.60, rely=0.55, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "100 บาท",fg="#000000" ,bg="#DEB887", width = 10,command = onehun_click).place(relx=0.75, rely=0.55, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = " ยืนยันการชำระเงิน",fg="#000000" ,bg="#DEB887", width = 10,command = end ).place(relx=0.70, rely=0.80, relwidth=0.15, relheight=0.08, anchor='n')
    
    Label(windows, textvariable=tv_total, bg="gold").place(relx=0.5, rely=0.8, relwidth=0.2, relheight=0.08 ,anchor='n')
    
    button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=sell)
    button2.place(relx=0.29, rely=0.8, relwidth=0.14, relheight=0.08,anchor='n')

    creator = tk.Frame(windows, bg='#006699', bd=6) 
    creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง

def ok1():
    tv_total.set(f'เงินที่ได้รับ = 0')
    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
    win_screen.place(relx=0.5, rely=0.27, relwidth=1.2, relheight=0.8, anchor='n')

    Name_Pro = str("โออิชิ")
    conn = sqlite3.connect("Databaseexample.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM users''')
    dataoutput = c.fetchall()
    for n in dataoutput :
        if Name_Pro == n[1] :
            Name = str(n[1])
            Price = str(n[2])
            Amount = str(n[3])
            Text = ("รายการ : "+Name+"\nราคา : "+Price+"\nจำนวนคงเหลือ : "+Amount)
            #print (Text)

    Label(windows,text=Text,fg="#000033",bg="#FAEBD7").place(relx=0.25, rely=0.32, relwidth=0.2, relheight=0.4, anchor='n')
    frame = tk.Frame(windows, bg='#FAFAD2',)
    frame.place(relx = 0.6, rely=0.32, relwidth=0.5, relheight=0.4, anchor='n')

    def one_click():
        one = 1
        savetotal[0] += 1
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def five_click():
        five = 5
        savetotal[0] += 5
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def ten_click():
        ten = 10
        savetotal[0] += 10
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def twen_click():
        twen = 20
        savetotal[0] += 20
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def fif_click():
        fif = 50
        savetotal[0] += 50
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def onehun_click():
        onehun = 100
        savetotal[0] += 100
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    Button(windows, text = "1 บาท",fg="#000000" ,bg="#FFD700", width = 10,command = one_click).place(relx=0.45, rely=0.40, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "5 บาท",fg="#000000" ,bg="#98FB98", width = 10,command = five_click).place(relx=0.60, rely=0.40, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "10 บาท",fg="#000000" ,bg="#66CDAA", width = 10,command = ten_click).place(relx=0.75, rely=0.40, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "20 บาท",fg="#000000" ,bg="#FFA07A", width = 10 ,command = twen_click).place(relx=0.45, rely=0.55, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "50 บาท",fg="#000000" ,bg="#9932CC", width = 10,command = fif_click).place(relx=0.60, rely=0.55, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "100 บาท",fg="#000000" ,bg="#DEB887", width = 10,command = onehun_click).place(relx=0.75, rely=0.55, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = " ยืนยันการชำระเงิน",fg="#000000" ,bg="#DEB887", width = 10,command = end).place(relx=0.75, rely=0.80, relwidth=0.15, relheight=0.08, anchor='n')

    Label(windows, textvariable=tv_total, bg="gold").place(relx=0.5, rely=0.8, relwidth=0.2, relheight=0.08 ,anchor='n')
    
    button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=sell)
    button2.place(relx=0.29, rely=0.8, relwidth=0.14, relheight=0.08,anchor='n')

    creator = tk.Frame(windows, bg='#006699', bd=6) 
    creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง

def ok2():
    tv_total.set(f'เงินที่ได้รับ = 0')
    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
    win_screen.place(relx=0.5, rely=0.27, relwidth=1.2, relheight=0.8, anchor='n')

    Name_Pro = str("สปอนเซอร์")
    conn = sqlite3.connect("Databaseexample.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM users''')
    dataoutput = c.fetchall()
    for n in dataoutput :
        if Name_Pro == n[1] :
            Name = str(n[1])
            Price = str(n[2])
            Amount = str(n[3])
            Text = ("รายการ : "+Name+"\nราคา : "+Price+"\nจำนวนคงเหลือ : "+Amount)
            #print (Text)

    Label(windows,text=Text,fg="#000033",bg="#FAEBD7").place(relx=0.25, rely=0.32, relwidth=0.2, relheight=0.4, anchor='n')
    frame = tk.Frame(windows, bg='#FAFAD2',)
    frame.place(relx = 0.6, rely=0.32, relwidth=0.5, relheight=0.4, anchor='n')

    def one_click():
        one = 1
        savetotal[0] += 1
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def five_click():
        five = 5
        savetotal[0] += 5
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def ten_click():
        ten = 10
        savetotal[0] += 10
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def twen_click():
        twen = 20
        savetotal[0] += 20
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def fif_click():
        fif = 50
        savetotal[0] += 50
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def onehun_click():
        onehun = 100
        savetotal[0] += 100
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    Button(windows, text = "1 บาท",fg="#000000" ,bg="#FFD700", width = 10,command = one_click).place(relx=0.45, rely=0.40, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "5 บาท",fg="#000000" ,bg="#98FB98", width = 10,command = five_click).place(relx=0.60, rely=0.40, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "10 บาท",fg="#000000" ,bg="#66CDAA", width = 10,command = ten_click).place(relx=0.75, rely=0.40, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "20 บาท",fg="#000000" ,bg="#FFA07A", width = 10 ,command = twen_click).place(relx=0.45, rely=0.55, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "50 บาท",fg="#000000" ,bg="#9932CC", width = 10,command = fif_click).place(relx=0.60, rely=0.55, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "100 บาท",fg="#000000" ,bg="#DEB887", width = 10,command = onehun_click).place(relx=0.75, rely=0.55, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = " ยืนยันการชำระเงิน",fg="#000000" ,bg="#DEB887", width = 10,command = end).place(relx=0.75, rely=0.80, relwidth=0.15, relheight=0.08, anchor='n')

    Label(windows, textvariable=tv_total, bg="gold").place(relx=0.5, rely=0.8, relwidth=0.2, relheight=0.08 ,anchor='n')
    
    button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=sell)
    button2.place(relx=0.29, rely=0.8, relwidth=0.14, relheight=0.08,anchor='n')

    creator = tk.Frame(windows, bg='#006699', bd=6) 
    creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง

def ok3():
    tv_total.set(f'เงินที่ได้รับ = 0')
    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
    win_screen.place(relx=0.5, rely=0.27, relwidth=1.2, relheight=0.8, anchor='n')

    Name_Pro = str("มาม่าบิ๊กต้มยำ")
    conn = sqlite3.connect("Databaseexample.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM users''')
    dataoutput = c.fetchall()
    for n in dataoutput :
        if Name_Pro == n[1] :
            Name = str(n[1])
            Price = str(n[2])
            Amount = str(n[3])
            Text = ("รายการ : "+Name+"\nราคา : "+Price+"\nจำนวนคงเหลือ : "+Amount)
            #print (Text)

    Label(windows,text=Text,fg="#000033",bg="#FAEBD7").place(relx=0.25, rely=0.32, relwidth=0.2, relheight=0.4, anchor='n')
    frame = tk.Frame(windows, bg='#FAFAD2',)
    frame.place(relx = 0.6, rely=0.32, relwidth=0.5, relheight=0.4, anchor='n')

    def one_click():
        one = 1
        savetotal[0] += 1
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def five_click():
        five = 5
        savetotal[0] += 5
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def ten_click():
        ten = 10
        savetotal[0] += 10
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def twen_click():
        twen = 20
        savetotal[0] += 20
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def fif_click():
        fif = 50
        savetotal[0] += 50
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def onehun_click():
        onehun = 100
        savetotal[0] += 100
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    Button(windows, text = "1 บาท",fg="#000000" ,bg="#FFD700", width = 10,command = one_click).place(relx=0.45, rely=0.40, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "5 บาท",fg="#000000" ,bg="#98FB98", width = 10,command = five_click).place(relx=0.60, rely=0.40, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "10 บาท",fg="#000000" ,bg="#66CDAA", width = 10,command = ten_click).place(relx=0.75, rely=0.40, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "20 บาท",fg="#000000" ,bg="#FFA07A", width = 10 ,command = twen_click).place(relx=0.45, rely=0.55, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "50 บาท",fg="#000000" ,bg="#9932CC", width = 10,command = fif_click).place(relx=0.60, rely=0.55, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "100 บาท",fg="#000000" ,bg="#DEB887", width = 10,command = onehun_click).place(relx=0.75, rely=0.55, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = " ยืนยันการชำระเงิน",fg="#000000" ,bg="#DEB887", width = 10,command = end).place(relx=0.75, rely=0.80, relwidth=0.15, relheight=0.08, anchor='n')

    Label(windows, textvariable=tv_total, bg="gold").place(relx=0.5, rely=0.8, relwidth=0.2, relheight=0.08 ,anchor='n')
    
    button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=sell)
    button2.place(relx=0.29, rely=0.8, relwidth=0.14, relheight=0.08,anchor='n')

    creator = tk.Frame(windows, bg='#006699', bd=6) 
    creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง

def ok4():
    tv_total.set(f'เงินที่ได้รับ = 0')
    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
    win_screen.place(relx=0.5, rely=0.27, relwidth=1.2, relheight=0.8, anchor='n')

    Name_Pro = str("มาม่าเย็นตาโฟ")
    conn = sqlite3.connect("Databaseexample.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM users''')
    dataoutput = c.fetchall()
    for n in dataoutput :
        if Name_Pro == n[1] :
            Name = str(n[1])
            Price = str(n[2])
            Amount = str(n[3])
            Text = ("รายการ : "+Name+"\nราคา : "+Price+"\nจำนวนคงเหลือ : "+Amount)
            #print (Text)

    Label(windows,text=Text,fg="#000033",bg="#FAEBD7").place(relx=0.25, rely=0.32, relwidth=0.2, relheight=0.4, anchor='n')
    frame = tk.Frame(windows, bg='#FAFAD2',)
    frame.place(relx = 0.6, rely=0.32, relwidth=0.5, relheight=0.4, anchor='n')

    def one_click():
        one = 1
        savetotal[0] += 1
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def five_click():
        five = 5
        savetotal[0] += 5
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def ten_click():
        ten = 10
        savetotal[0] += 10
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def twen_click():
        twen = 20
        savetotal[0] += 20
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def fif_click():
        fif = 50
        savetotal[0] += 50
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def onehun_click():
        onehun = 100
        savetotal[0] += 100
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    Button(windows, text = "1 บาท",fg="#000000" ,bg="#FFD700", width = 10,command = one_click).place(relx=0.45, rely=0.40, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "5 บาท",fg="#000000" ,bg="#98FB98", width = 10,command = five_click).place(relx=0.60, rely=0.40, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "10 บาท",fg="#000000" ,bg="#66CDAA", width = 10,command = ten_click).place(relx=0.75, rely=0.40, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "20 บาท",fg="#000000" ,bg="#FFA07A", width = 10 ,command = twen_click).place(relx=0.45, rely=0.55, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "50 บาท",fg="#000000" ,bg="#9932CC", width = 10,command = fif_click).place(relx=0.60, rely=0.55, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "100 บาท",fg="#000000" ,bg="#DEB887", width = 10,command = onehun_click).place(relx=0.75, rely=0.55, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = " ยืนยันการชำระเงิน",fg="#000000" ,bg="#DEB887", width = 10,command = end).place(relx=0.75, rely=0.80, relwidth=0.15, relheight=0.08, anchor='n')

    Label(windows, textvariable=tv_total, bg="gold").place(relx=0.5, rely=0.8, relwidth=0.2, relheight=0.08 ,anchor='n')
    
    button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=sell)
    button2.place(relx=0.29, rely=0.8, relwidth=0.14, relheight=0.08,anchor='n')

    creator = tk.Frame(windows, bg='#006699', bd=6) 
    creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง

def ok5():
    tv_total.set(f'เงินที่ได้รับ = 0')
    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
    win_screen.place(relx=0.5, rely=0.27, relwidth=1.2, relheight=0.8, anchor='n')

    Name_Pro = str("มาม่าหมูต้มยำ")
    conn = sqlite3.connect("Databaseexample.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM users''')
    dataoutput = c.fetchall()
    for n in dataoutput :
        if Name_Pro == n[1] :
            Name = str(n[1])
            Price = str(n[2])
            Amount = str(n[3])
            Text = ("รายการ : "+Name+"\nราคา : "+Price+"\nจำนวนคงเหลือ : "+Amount)
            #print (Text)

    Label(windows,text=Text,fg="#000033",bg="#FAEBD7").place(relx=0.25, rely=0.32, relwidth=0.2, relheight=0.4, anchor='n')
    frame = tk.Frame(windows, bg='#FAFAD2',)
    frame.place(relx = 0.6, rely=0.32, relwidth=0.5, relheight=0.4, anchor='n')

    def one_click():
        one = 1
        savetotal[0] += 1
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def five_click():
        five = 5
        savetotal[0] += 5
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def ten_click():
        ten = 10
        savetotal[0] += 10
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def twen_click():
        twen = 20
        savetotal[0] += 20
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def fif_click():
        fif = 50
        savetotal[0] += 50
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    def onehun_click():
        onehun = 100
        savetotal[0] += 100
        tv_total.set(f'เงินที่ได้รับ = {savetotal[0]}')

    Button(windows, text = "1 บาท",fg="#000000" ,bg="#FFD700", width = 10,command = one_click).place(relx=0.45, rely=0.40, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "5 บาท",fg="#000000" ,bg="#98FB98", width = 10,command = five_click).place(relx=0.60, rely=0.40, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "10 บาท",fg="#000000" ,bg="#66CDAA", width = 10,command = ten_click).place(relx=0.75, rely=0.40, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "20 บาท",fg="#000000" ,bg="#FFA07A", width = 10 ,command = twen_click).place(relx=0.45, rely=0.55, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "50 บาท",fg="#000000" ,bg="#9932CC", width = 10,command = fif_click).place(relx=0.60, rely=0.55, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "100 บาท",fg="#000000" ,bg="#DEB887", width = 10,command = onehun_click).place(relx=0.75, rely=0.55, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = " ยืนยันการชำระเงิน",fg="#000000" ,bg="#DEB887", width = 10,command = end).place(relx=0.75, rely=0.80, relwidth=0.15, relheight=0.08, anchor='n')

    Label(windows, textvariable=tv_total, bg="gold").place(relx=0.5, rely=0.8, relwidth=0.2, relheight=0.08 ,anchor='n')
    
    button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=sell)
    button2.place(relx=0.29, rely=0.8, relwidth=0.14, relheight=0.08,anchor='n')

    creator = tk.Frame(windows, bg='#006699', bd=6) 
    creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง

def end():
    amount_del = int(changmoney[1])-1
    name_product = str(changmoney[2])
    print(amount_del)
    print(name_product)
    win_screen = tk.Frame(windows, bg= '#f0f0f0', bd=5)
    win_screen.place(relx=0.5, rely=0.27, relwidth=1.2, relheight=0.8, anchor='n')
    Label(windows,text="เงินทอนของคุณ").place(relx=0.5, rely=0.27, relwidth=0.2, relheight=0.1, anchor='n')
    #print (total_bt)

    price = float(savetotal[0])
    get = float(changmoney[0])
    if(price<get):
        messagebox.showinfo(title="การแจ้งเตือน",message="ขออภัยค่ะ ยอดเงินของคุณ ไม่พอสำหรับการใช้บริการนี้")
        sell()
    else:
        chang = float(price - get)
        print("price = "+str(price))
        print("get = "+str(get))
        print("price - get = "+str(chang))
        conn = sqlite3.connect('Databaseexample.db')
        c = conn.cursor()
        #data = (num1,pric1,amou1,prod1)
        sql = 'UPDATE users SET amount = "{}" WHERE Products = "{}"'.format(str(amount_del),name_product)
        print(sql)
        c.execute(sql)
        conn.commit() 
        conn.close()

        Label(windows,text=chang,bg="#FFC0CB",fg='#000000').place(relx=0.50, rely=0.37, relwidth=0.3, relheight=0.3,anchor='n')
        ### ข้างบนโค้ดเงินทอน
        button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=home)
        button2.place(relx=0.50, rely=0.8, relwidth=0.19, relheight=0.08,anchor='n')

        creator = tk.Frame(windows, bg='#006699', bd=6) 
        creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง

def chang():
    win_screen = tk.Frame(windows)
    win_screen.place(relx=0.5, rely=0.27, relwidth=1.2, relheight=0.8, anchor='n')


    Label(windows,text="เลือกธนบัตรที่ต้องการแลก").place(relx=0.5, rely=0.29, relwidth=0.2, relheight=0.1, anchor='n')

    frame = tk.Frame(windows, bg='#FAFAD2',)
    frame.place(relx = 0.5, rely=0.37, relwidth=0.5, relheight=0.4, anchor='n')
    
    Button(windows, text = "20 บาท",fg="#000000" ,bg="#98FB98", width = 10 ,command=chang20).place(relx=0.33, rely=0.45, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "50 บาท",fg="#000000" ,bg="#66CDAA", width = 10,command=chang50).place(relx=0.5, rely=0.45, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "100 บาท",fg="#000000" ,bg="#FFA07A", width = 10,command=chang100 ).place(relx=0.67, rely=0.45, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "500 บาท",fg="#000000" ,bg="#9932CC", width = 10,command=chang500).place(relx=0.43, rely=0.6, relwidth=0.1, relheight=0.1, anchor='n')
    Button(windows, text = "1000 บาท",fg="#000000" ,bg="#DEB887", width = 10,command=chang1000).place(relx=0.57, rely=0.6, relwidth=0.1, relheight=0.1, anchor='n')

    button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=home)
    button2.place(relx=0.50, rely=0.8, relwidth=0.19, relheight=0.08,anchor='n')

    creator = tk.Frame(windows, bg='#006699', bd=6) 
    creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง

def chang20():
    kind=[]
    win_screen = tk.Frame(windows)
    win_screen.place(relx=0.5, rely=0.27, relwidth=1.2, relheight=0.8, anchor='n')

    Label(windows,text="แลกเงินสำเร็จ").place(relx=0.5, rely=0.27, relwidth=0.2, relheight=0.1, anchor='n')
    money = int(20)
    for t in moneytype:
        if money > t:
            x = ("{:<5}บาท\tจำนวน\t{:<10}".format(t , int(money / t)))
            #print(x)
            kind.append(x)
            total = money % t
    Label(windows,text="อัตราการแลกเงิน\n"+kind[1]+"\n"+kind[2]+"\n"+kind[3]
        ,bg="#D2691E",fg='#FFFFFF').place(relx=0.50, rely=0.37, relwidth=0.4, relheight=0.4,anchor='n')


    button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=home)
    button2.place(relx=0.40, rely=0.8, relwidth=0.19, relheight=0.08,anchor='n')
    button3 = tk.Button(windows,text='แลกอีกครั้ง',bg="#6A5ACD",fg='#FFFFFF',command=chang)
    button3.place(relx=0.62, rely=0.8, relwidth=0.15, relheight=0.08,anchor='n')

    creator = tk.Frame(windows, bg='#006699', bd=6) 
    creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง

def chang50():
    kind=[]
    win_screen = tk.Frame(windows)
    win_screen.place(relx=0.5, rely=0.27, relwidth=1.2, relheight=0.8, anchor='n')

    Label(windows,text="แลกเงินสำเร็จ").place(relx=0.5, rely=0.27, relwidth=0.2, relheight=0.1, anchor='n') 
    money = int(50)
    for t in moneytype:
        if money > t:
            x = ("{:<5}บาท\tจำนวน\t{:<10}".format(t , int(money / t)))
            #print(x)
            kind.append(x)
            total = money % t
    Label(windows,text="อัตราการแลกเงิน\n"+kind[1]+"\n"+kind[2]+"\n"+kind[3]+"\n"+kind[4]
        ,bg="#D2691E",fg='#FFFFFF').place(relx=0.50, rely=0.37, relwidth=0.4, relheight=0.4,anchor='n')

    button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=home)
    button2.place(relx=0.40, rely=0.8, relwidth=0.19, relheight=0.08,anchor='n')
    button3 = tk.Button(windows,text='แลกอีกครั้ง',bg="#6A5ACD",fg='#FFFFFF',command=chang)
    button3.place(relx=0.62, rely=0.8, relwidth=0.15, relheight=0.08,anchor='n')

    creator = tk.Frame(windows, bg='#006699', bd=6) 
    creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง

def chang100():
    kind=[]
    win_screen = tk.Frame(windows)
    win_screen.place(relx=0.5, rely=0.27, relwidth=1.2, relheight=0.8, anchor='n')

    Label(windows,text="แลกเงินสำเร็จ").place(relx=0.5, rely=0.27, relwidth=0.2, relheight=0.1, anchor='n')
    money = int(100)
    for t in moneytype:
        if money > t:
            x = ("{:<5}บาท\tจำนวน\t{:<10}".format(t , int(money / t)))
            #print(x)
            kind.append(x)
            total = money % t
    Label(windows,text="อัตราการแลกเงิน\n"+kind[1]+"\n"+kind[2]+"\n"+kind[3]+"\n"+kind[4]+"\n"+kind[5]
        ,bg="#D2691E",fg='#FFFFFF').place(relx=0.50, rely=0.37, relwidth=0.4, relheight=0.4,anchor='n')
   
    button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=home)
    button2.place(relx=0.40, rely=0.8, relwidth=0.19, relheight=0.08,anchor='n')
    button3 = tk.Button(windows,text='แลกอีกครั้ง',bg="#6A5ACD",fg='#FFFFFF',command=chang)
    button3.place(relx=0.62, rely=0.8, relwidth=0.15, relheight=0.08,anchor='n')

    creator = tk.Frame(windows, bg='#006699', bd=6) 
    creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง

def chang500():
    kind=[]
    win_screen = tk.Frame(windows)
    win_screen.place(relx=0.5, rely=0.27, relwidth=1.2, relheight=0.8, anchor='n')

    Label(windows,text="แลกเงินสำเร็จ").place(relx=0.5, rely=0.27, relwidth=0.2, relheight=0.1, anchor='n')

    money = int(500)
    for t in moneytype:
        if money > t:
            x = ("{:<5}บาท\tจำนวน\t{:<10}".format(t , int(money / t)))
            #print(x)
            kind.append(x)
            total = money % t
    Label(windows,text="อัตราการแลกเงิน\n"+kind[1]+"\n"+kind[2]+"\n"+kind[3]+"\n"+kind[4]+"\n"+kind[5]+"\n"+kind[6]
        ,bg="#D2691E",fg='#FFFFFF').place(relx=0.50, rely=0.37, relwidth=0.4, relheight=0.4,anchor='n')

    button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=home)
    button2.place(relx=0.40, rely=0.8, relwidth=0.19, relheight=0.08,anchor='n')
    
    button3 = tk.Button(windows,text='แลกอีกครั้ง',bg="#6A5ACD",fg='#FFFFFF',command=chang)
    button3.place(relx=0.62, rely=0.8, relwidth=0.15, relheight=0.08,anchor='n')

    creator = tk.Frame(windows, bg='#006699', bd=6) 
    creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง

def chang1000():
    kind=[]
    win_screen = tk.Frame(windows)
    win_screen.place(relx=0.5, rely=0.27, relwidth=1.2, relheight=0.8, anchor='n')

    Label(windows,text="แลกเงินสำเร็จ").place(relx=0.5, rely=0.27, relwidth=0.2, relheight=0.1, anchor='n')

    money = int(1000)
    for t in moneytype:
        if money > t:
            x = ("{:<5}บาท\tจำนวน\t{:<10}".format(t , int(money / t)))
            #print(x)
            kind.append(x)
            total = money % t
    Label(windows,text="อัตราการแลกเงิน\n"+kind[1]+"\n"+kind[2]+"\n"+kind[3]+"\n"+kind[4]+"\n"+kind[5]+"\n"+kind[6]+"\n"+kind[7]
        ,bg="#D2691E",fg='#FFFFFF').place(relx=0.50, rely=0.37, relwidth=0.4, relheight=0.4,anchor='n')
   
    button2 = tk.Button(windows,text='กลับหน้าหลัก',bg="#2E8B57",fg='#FFFFFF',command=home)
    button2.place(relx=0.38, rely=0.8, relwidth=0.15, relheight=0.08,anchor='n')

    button3 = tk.Button(windows,text='แลกอีกครั้ง',bg="#6A5ACD",fg='#FFFFFF',command=chang)
    button3.place(relx=0.62, rely=0.8, relwidth=0.15, relheight=0.08,anchor='n')

    creator = tk.Frame(windows, bg='#006699', bd=6) 
    creator.place(relx=0.5, rely=0.9, relwidth=0.57, relheight=0.06, anchor='n') #กรอบล่าง

def base():
    photo = PhotoImage(file="ปก6.png")
    Button(windows, image = photo, borderwidth=0).pack()
    head()
    create_()
    home()
    windows.mainloop()


boxID = StringVar()
boxpro = StringVar()
boxprice = StringVar()
boxam = StringVar()

one_bt = 0
five_bt = 0
ten_bt = 0
twenty_bt = 0
fif_bt = 0
onehun_bt = 0
total_bt = 0

tv_one = IntVar()
tv_five = IntVar()
tv_ten = IntVar()
tv_twenty = IntVar()
tv_fif = IntVar()
tv_onehund = IntVar()
tv_total = StringVar()

savetotal = [0]
changmoney = []

base()