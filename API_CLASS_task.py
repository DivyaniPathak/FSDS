from flask import Flask, request, jsonify




app = Flask(__name__)

@app.route('/DB_CALL_showDB',methods=['GET','POST'])
def test1():
    import mysql.connector as connection
    mydb = connection.connect(host = "localhost",
                          user = "root",
                          passwd = "Diva#294")
    cursor = mydb.cursor()
    cursor.execute("create database TMP1_API")
    cursor.execute("show databases")
    return(cursor.fetchall())

@app.route('/DB_CALL_insert',methods=['GET','POST'])
def test2():
    import mysql.connector as connection
    mydb = connection.connect(host = "localhost",
                          user = "root",
                          passwd = "Diva#294")
    cursor = mydb.cursor()
    s = "insert into tmp_api.ineuron1 values(101 , 'divyani pathak', 'pathak@gmail.com' ,7000 , 30)"
    cursor.execute(s)
    mydb.commit()
    return(cursor.fetchall())


@app.route('/DB_CALL_update',methods=['GET','POST'])
def test3():
    import mysql.connector as connection
    mydb = connection.connect(host = "localhost",
                          user = "root",
                          passwd = "Diva#294")
    cursor = mydb.cursor()
    s = "update tmp_api.ineuron1 set emp_name = 'shruti' where employe_id = 101"
    cursor.execute(s)
    mydb.commit()
    return(cursor.fetchall())


@app.route('/DB_CALL_delete',methods=['GET','POST'])
def test4():
    import mysql.connector as connection
    mydb = connection.connect(host = "localhost",
                          user = "root",
                          passwd = "Diva#294")
    cursor = mydb.cursor()
    s = "delete from tmp_api.ineuron1 where emp_name = 'shruti' "
    cursor.execute(s)
    mydb.commit()
    return(cursor.fetchall())


@app.route('/DB_CALL_select',methods=['GET','POST'])
def test5():
    import mysql.connector as connection
    mydb = connection.connect(host = "localhost",
                          user = "root",
                          passwd = "Diva#294")
    cursor = mydb.cursor()
    s = "select * from tmp_api.ineuron1 "
    cursor.execute(s)
    return(cursor.fetchall())

if __name__=='__main__' :
    app.run()