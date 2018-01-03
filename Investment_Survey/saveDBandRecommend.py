#!/usr/bin/env python36
import cgi
import cgitb
import CookieFunction
import pymysql as mydb
#import mysql.connector as mydb             #Mysql 2x database driver
import re                                   #regular expressions
cgitb.enable()



print("Content-Type: text/html \n")
#page1 cookie
firstname = CookieFunction.getCookie('firstname');
lastname = CookieFunction.getCookie('lastname');
age = CookieFunction.getCookie('age');
gender = CookieFunction.getCookie('gender');
education = CookieFunction.getCookie('education');
marriage = CookieFunction.getCookie('marriage');
income = CookieFunction.getCookie('income');

#page2 cookie
investAmount = CookieFunction.getCookie('investAmount');
objective = CookieFunction.getCookie('objective');
security = CookieFunction.getCookie('security');
industry = CookieFunction.getCookie('industry');
time = CookieFunction.getCookie('time');

#page3cookie
hypo_port = CookieFunction.getCookie('hypo_port');
price_drop = CookieFunction.getCookie('price_drop');
price_soar = CookieFunction.getCookie('price_soar');
inflation = CookieFunction.getCookie('inflation');

msg=''




# save to database
def saveDB():
    global msg
    # first column is form_id, I set it incremental. so add a '0' at the very beginning of the insert statement.
    sql = "insert into team6_form_data "
    sql += "values(" + str(0) + ",'" + firstname + "','" + lastname + "','" \
           + age + "','" + gender + "','" + education + "','" + marriage + "','" + income + "','" \
           + investAmount + "','" + objective + "','" + security + "','" + industry + "','" \
           + time + "','" + hypo_port + "','" + price_drop + "','" + price_soar + "','" + inflation + "')"
    try:

        conn = mydb.connect(host='localhost',user='team6',password='team6',database='team6')
        cursor = conn.cursor()
        cursor.execute(sql);
        conn.commit()

    except mydb.Error as e:
        (errorNum, errorMsg) = e.args
        msg = 'Database Error-' + str(errorNum) + errorMsg
        return

    cursor.close()
    conn.close()

data=[]
#recommendation function
def matchRecommend():
    try:
        conn = mydb.connect(host='localhost',user='team6',password='team6',database='team6')
        cursor = conn.cursor()  # create a cursor
        sql = "SELECT product_name "
        sql += " FROM recommend_product "
        sql += " where price_drop='"+price_drop+"' AND price_soar='"+price_soar+"' AND inflation='"+inflation+"'"

        result = cursor.execute(sql);  # execute the query

    except mydb.Error as e:
        errorNum = e.args[0]
        errorMsg = e.args[1]
        error = 'Database Error - ' + str(errorNum) + errorMsg
        return

    row = cursor.fetchone()                #get one row at a time
    data.append(row)

    cursor.close()
    conn.close()

#display functions

def display():
    print("<html><head><link rel='stylesheet' type='text/css' href='survey.css'><body><header>")
    print("<center><h1>&nbsp;Investment Preference Survey</h1></center>")
    print('</header>')
    print("<br><br>")
    print("<center><h1 style='color: darkgreen'>Your survey is completed!</h1>")
    print("<center><h2 style='color: darkgreen'>According to our database, we recommend you the following product</h2>")
    print("<table border=1 style='color: white'><tr><td> Name of Recommend Product: &nbsp</td><td> ")
    for row in data:
        product_name = row[0]
    print( product_name +" </td></tr></table></center>")
    print('<br><br><br><br><footer>Copyright &copy; Team 6 </footer>')
    print('</body>')
    print('</head>')
    print('</html>')


# call functions
if msg=='':
    saveDB()
    matchRecommend()
    display()
