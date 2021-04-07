import sqlite3

def insertTousers (fname,lName,email) :
    try :
        conn = sqlite3.connect (r"C:\Users\ACER\Documents\Piamsuk_Python\Week6\Week6.1.db")
        c = conn.cursor()

        sql = """INSERT INTO users (fname,lName,email) VALUES (?,?,?)"""
        data = (fname,lName,email)
        c.execute(sql,data)
        conn.commit()
        c.close()

    except sqlite3.Error as e:
        print("Faild to insert : ",e)
    finally :

        if conn :
            conn.close()
insertTousers("Kim","Soekjin","Soekjin@gmail.com")
insertTousers("Kim","Namjon","Namjon@gmail.com")