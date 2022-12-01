import sqlite3 #importing sqlite3 so it can be used

conn = sqlite3.connect('submit.db') #creating the database file

#creating the database and adding columns as well as commiting them
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_contact( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_phonenum TEXT, \
        col_email TEXT \
        )")
    conn.commit()
conn.close() #closing the connection to avoid a memory leak


conn = sqlite3.connect('submit.db') #opening up the connection again

#creating the database and adding values to our columns as well as commiting them
with conn:
    cur = conn.cursor()
    #inserting values with execute
    cur.execute("INSERT INTO tbl_contact(col_fname,col_phonenum,col_email) VALUES (?,?,?)",
                ('Dan','458-222-9863','dhowell@gmail.com'))
    cur.execute("INSERT INTO tbl_contact(col_fname,col_phonenum,col_email) VALUES (?,?,?)",
                ('Jane','541-232-5041','janef@gmail.com'))
    cur.execute("INSERT INTO tbl_contact(col_fname,col_phonenum,col_email) VALUES (?,?,?)",
                ('Mary','458-856-0000','mary22@gmail.com'))
    conn.commit()
conn.close()#closing the connection again

conn = sqlite3.connect('submit.db')
#querying something from the data base so it can print directly in python shell

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname,col_phonenum,col_email FROM tbl_contact WHERE col_fname = 'Jane'")
    #variable will be used to store the data grabbed
    varContact = cur.fetchall()
    for item in varContact:
        msg = "First name: {}\nPhone Number: {}\nEmail: {}".format(item[0],item[1],item[2])
    print(msg)
    #printing the result of varContact using variable msg



fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg', 'World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('submit.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_contact VALUES (?);", [','.join(fileList)])


#trying to create a function that will iterate through the files to check
#for text only
res = [] #var to hold result

for x in fileList:
    if x.endswith('.txt'):
        res.append(x)
    print(res)
