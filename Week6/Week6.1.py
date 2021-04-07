import sqlite3 #import sqlite
conn = sqlite3.connect(r"C:\Users\ACER\Documents\Piamsuk_Python\Week6\Week6.1.db")
c = conn.cursor() #create a cursor object
'''c.execute (""" CREATE TABLE users(id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(30) NOT NULL,
    lName varchar(30) NOT NULL,
    email varchar(100) NOT NULL)""")
'''
c.execute(""" INSERT INTO users (id,fname,lName,email) VALUES (NULL,"Piamsuk" ,"Wa", "Piamsuk@kkumail.com")""")
c.execute(""" INSERT INTO users VALUES (NULL,"Jackson" ,"Wang", "Jacksonwa@gmail.com")""")
c.execute(""" INSERT INTO users VALUES (NULL,"Taehyung" ,"Kim", "kimtaehyung@gmail.com")""")
c.execute(""" INSERT INTO users VALUES (NULL,"Jaebeom" ,"Lim", "Limjaebeom@gmail.com")""")
c.execute(""" INSERT INTO users VALUES (NULL,"Mark" ,"Tuan", "Mark.tuan@gmail.com")""")
conn.commit() #save (commit) the change
conn.close() #close the connection when done