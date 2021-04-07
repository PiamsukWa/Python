import sqlite3 

conn = sqlite3.connect(r"C:\Users\ACER\Documents\Piamsuk_Python\Week6\Week6.1.db")
c = conn.cursor()

try : 
    c.execute('SELECT * FROM users ORDER BY id DESC')
    conn.commit()
    result = c.fetchall()
    for i in result :
        print(i)
    c.close

except sqlite3.Error as e:
    print(e)

finally :
    if conn :
        conn.close()