
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





with conn:
    cur = conn.cursor()
    for file in fileList:
        if file.endswith(".txt"):
            cur.execute("INSERT INTO tbl_documents(col_fileList) VALUES (?)",
                        (file,))
            print(file)
    conn.commit()
conn.close()

