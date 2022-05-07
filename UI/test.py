from flask import Flask, render_template,request,json,redirect
from flask_table import Table, Col
import pymysql.cursors
loginidg=""
templist=[]
class Results(Table):
    id = Col('Id', show=False)
    VehicleName = Col('VehicleName')
    Numplate = Col('Numplate')
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='dbtest',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
app = Flask(__name__)
@app.route("/get-reg")
def signuppage():
    return render_template('register.html')
@app.route('/save-post',methods=['POST', 'GET'])
def signUp():
    if request.method=='POST':
     loginid=request.form['id']
     fname=request.form['fname']
     lname=request.form['lname']
     number=request.form['number']
     email=request.form['email']
     password=request.form['password']
     try:
  

      with connection.cursor() as cursor:
      # Read a single record
        sql = "INSERT INTO registration (LoginID,FirstName,LastName,EmailID,ContactNo,Password) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (loginid,fname,lname,email,number,password))
        connection.commit()
     finally:
      connection.close()
      return "Saved successfully."
    else:
      return "error"
@app.route("/login")
def loginpage():
    return render_template('login.html')
@app.route("/logincheck",methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        loginid=request.form['uname']
        password=request.form['passw']
        temp=loginid.encode('ascii','ignore')
        global loginidg
        loginidg=temp
        with connection.cursor() as cursor:
            sql = "SELECT * from `registration` WHERE `LoginID`=%s AND `Password`=%s"
            cursor.execute(sql, (loginid,password,))
            result = cursor.fetchone()
            if result is None:
                return render_template('login.html')
            else:
                with connection.cursor() as cursor:
                    sql = "SELECT `VehicleName`,`Numplate` from `vehicle` WHERE `LoginID`=%s"
                    cursor.execute(sql, (loginid, ))
                    result = cursor.fetchall()
                    l1=list(result)
                    l2=[]
                    table = Results(result)
                    table.border = True
                    global templist
                    for i in l1:
                        for j in i:
                            l2.append(i[j])
                    templist=l2
                    return render_template('index.html',user=loginidg,your_list=result,table=table)
@app.route("/vehreg")
def vehregpage():
    return render_template('vehiclereg.html')
@app.route("/vehregr",methods=['POST', 'GET'])
def vehreg():
    if request.method=='POST':
        nplate=request.form['nplate']
        vname=request.form['vname']
        with connection.cursor() as cursor:
            sql = "INSERT INTO vehicle (Numplate,VehicleName,LoginID) VALUES (%s,%s,(select LoginID from registration where `LoginID`=%s))  "
            cursor.execute(sql, (nplate,vname,loginidg))
            connection.commit()
            return redirect("http://localhost:5000/login")
@app.route("/vehdel")
def vehdelpage():
    return render_template('vehdel.html')
@app.route("/vehdeld",methods=['POST', 'GET'])
def vehdel():
     if request.method=='POST':
         nplate=request.form['nplate']
         with connection.cursor() as cursor:
             sql = "DELETE from vehicle where `Numplate` = %s"
             cursor.execute(sql, (nplate))
             connection.commit()
             return redirect("http://localhost:5000/login")
@app.route("/check")
def check():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `registration` WHERE `LoginID`=%s"
        cursor.execute(sql, ('hetshah25',))
        result=cursor.fetchone()
        return render_template('string.html',your_list=result)
@app.route("/check2")
def check2():
    l1=['1','2','3','4']
    return render_template('string.html',your_list=l1)
if __name__ == "__main__":
    app.run()