
import sqlite3

conn = sqlite3.connect('assignmentpy.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_documents ( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fileList STRING \
            )")
    conn.commit()
conn.close()

conn = sqlite3.connect('assignmentpy.db')

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
#Variable created with desired files to iterate through.





with conn:
    cur = conn.cursor()
    for file in fileList:
        #temp variable file created for fileList variable 
        if file.endswith(".txt"):
            #specifically targeting files that end with the .txt 
            cur.execute("INSERT INTO tbl_documents(col_fileList) VALUES (?)",
                        (file,)) #for all of the files with the desired value input them into the table                    
            print(file)
    conn.commit()
conn.close()

