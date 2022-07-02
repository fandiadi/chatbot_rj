from unittest import result
import mysql.connector

#Define and Connection#
mydb = mysql.connector.connect(
    host="localhost", database='chatbot_rj', user="root", passwd="", use_pure=True)


class database():
    #Query#
    def query(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM tbl_data")
        myresult = mycursor.fetchall()
        return myresult

    def kelas(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT count(jenis_poli) FROM tbl_data")
        myresult = mycursor.fetchall()
        return myresult

    def count(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT count(jenis_poli) FROM tbl_data")
        myresult = mycursor.fetchall()
        return myresult

    #result = mycursor.execute("SELECT * FROM tbl_data")
    # return result
