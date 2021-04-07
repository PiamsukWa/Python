import sqlite3 
conn = sqlite3.connect(r"C:\Users\ACER\Documents\Piamsuk_Python\Week6\Week6.1.db")
c = conn.cursor() 
try : 
    data = ("Nook","Nick","Noolnick@gmail.com"),("Bom","Bam","Bombam@gmail.com"),("Plaii","Fah","Plaiifah@gmail.com")
    c.execute("INSERT INTO users (fname,lName,email) VALUES (?,?,?)",data)
    conn.commit()
    c.close()
except sqlite3.Error as e :
    print(e)

finally :
    if conn :
        conn.close() 
