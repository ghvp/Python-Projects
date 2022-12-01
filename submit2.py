import sqlite3 #importing sqlite3 so it can be used

conn = sqlite3.connect("files.db") #creating the database file

#adding columns
with conn:
    cur = conn.cursor()
    #adding in some columns 
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_fileName \
        )")
    conn.commit() #commiting changes to the database
conn.close() #closing the connection



conn = sqlite3.connect('files.db') #opening up the connection again

#adding values to our columns as well as commiting them
with conn:
    cur = conn.cursor()
    #trying to create a function that will iterate through the files to check
    #for text only
    fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg', 'World.txt','data.pdf','myPhoto.jpg')
    for x in fileList:
        if x.endswith('.txt'):
            cur.execute("INSERT INTO tbl_files(col_fileName) VALUES (?)",
                        (x,))
    conn.commit()
conn.close()

#printing db to the shell

conn = sqlite3.connect('files.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_files")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    

        


    

























