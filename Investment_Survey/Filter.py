#!/usr/bin/env python36
#=====================================================================================
# Get data from a database
# Display to an html form
# Allow filtering through the data

import cgi
import cgitb
import pymysql as mydb
import re

cgitb.enable()

data = []

print("Content-Type: text/html \n")

def read_data():

    global Goal, edu, retirement, health
    global equity, derivative, debt
    global fin, uti, tech, consume, ene, health_ind, tele, mat

    elements   = cgi.FieldStorage()

    Goal = elements.getvalue('objective1') or ""
    edu = elements.getvalue('objective2') or ""
    retirement = elements.getvalue('objective3') or ""
    health = elements.getvalue('objective4') or ""

    debt = elements.getvalue('security1') or ""
    equity = elements.getvalue('security2') or ""
    derivative = elements.getvalue('security3') or ""

    fin = elements.getvalue('industry1') or ""
    uti = elements.getvalue('industry2') or ""
    consume = elements.getvalue('industry3') or ""
    ene = elements.getvalue('industry4') or ""
    health_ind = elements.getvalue('industry5') or ""
    tech  = elements.getvalue('industry6')  or ""
    tele = elements.getvalue('industry7') or ""
    mat = elements.getvalue('industry8') or ""

    host   = 'localhost'
    port   =  3306
    userid = 'team6'
    pswd   = 'team6'
    db     = 'team6'

    try:
        conn = mydb.connect(host=host,user=userid,password=pswd,database=db)

        cursor = conn.cursor()

        filter = ""
        if Goal : filter += "Investment_Objective  like '%" + Goal + "%' AND "
        if edu : filter += "Investment_Objective  like '%" + edu + "%' AND "
        if retirement : filter += "Investment_Objective like '%" + retirement + "%' AND "
        if health : filter += "Investment_Objective  like '%" + health + "%' AND "

        if equity : filter += "Security_Type  like '%" + equity + "%' AND "
        if derivative : filter += "Security_Type  like '%" + derivative + "%' AND "
        if debt : filter += "Security_Type  like '%" + debt + "%' AND "

        if fin : filter += "Industry_Preference like '%" + fin + "%' AND "
        if uti : filter += "Industry_Preference like '%" + uti + "%' AND "
        if tech  : filter += "Industry_Preference like '%" + tech  + "%' AND "
        if consume : filter += "Industry_Preference like '%" + consume + "%' AND "
        if ene : filter += "Industry_Preference like '%" + ene + "%' AND "
        if health_ind : filter += "Industry_Preference like '%" + health_ind + "%' AND "
        if tele : filter += "Industry_Preference like '%" + tele + "%' AND "
        if mat : filter += "Industry_Preference like '%" + mat + "%' AND "
        filter += "1=1"                                                         #catch all in case no filter

        sql  = "SELECT Fname,Lname,Age, Highest_Education, Annual_Income, Investment_Objective, Security_Type, Industry_Preference " \
             + "FROM team6_form_data "  \
             + "WHERE 1=1 AND ("+ filter +")"



        result = cursor.execute(sql);

    except mydb.Error as e:
        errorNum = e.args[0]
        errorMsg = e.args[1]
        error = 'Database Error - ' + str(errorNum) + errorMsg
        return

    i=0
    row = cursor.fetchone()                         #get first row
    while row is not None:
        data.append(row)
        i+=1
        row = cursor.fetchone()                     #get next row

    cursor.close()                                  #close the cursor/buffer
    conn.close()                                    #close the connection



# display: display data

def display():

    global Goal, edu, retirement, health
    global equity, derivative, debt
    global fin, uti, tech, consume, ene, health_ind, tele, mat

    print("""
        <html>
        <head>
    <title>Filter_Investment Preference Survey</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" type="text/css" href="survey.css">
        </head>
    <body>
    <header>
    <h1><i class="material-icons">border_color</i>&nbsp;Filter the Survey Results&nbsp;<i class="material-icons">insert_chart</i></h1><br>
    </header>
        <br>
    &nbsp;
    <center><a href='Admin_SearchSortFilter.html'><input type=button value='   Go Back   '></a></center>
    <div class="text">
        <form action=Filter.py method=GET>
    """)
    print('<table><tr><td><b>Investment_Objective(s)')
    print("<td><input type=checkbox name=objective1 value='Goal'", end='')
    if Goal : print('checked', end='')
    print('>Financial Goal')
    print("<td><input type=checkbox name=objective2 value='edu'", end='')
    if edu : print('checked', end='')
    print('>Education')
    print("<td><input type=checkbox name=objective3 value='retirement'",end='')
    if retirement : print('checked',end='')
    print('>Retirement')
    print("<td><input type=checkbox name=objective4 value='health'", end='')
    if health : print('checked', end='')
    print('>Healthcare')

    print('<tr><td><b>Security Type(s)')
    print("<td><input type=checkbox name=security1 value='debt'",end='')
    if debt : print('checked', end='')
    print('>Debt')
    print("<td><input type=checkbox name=security2 value='equity'",end='')
    if equity : print('checked', end='')
    print('>Equity')
    print("<td><input type=checkbox name=security3 value='derivative'",end='')
    if derivative: print('checked', end='')
    print('>Derivative')

    print('<tr><td><b>Industry Preference(s)')
    print("<td><input type=checkbox name=industry1 value='fin'",end='')
    if fin : print('checked', end='')
    print('>Financial')
    print("<td><input type=checkbox name=industry2 value='uti'",end='')
    if uti: print('checked', end='')
    print('>Utility')
    print("<td><input type=checkbox name=industry3 value='consume'",end='')
    if consume : print('checked', end='')
    print('>Consumer')
    print("<td><input type=checkbox name=industry4 value='ene'",end='')
    if ene : print('checked', end='')
    print('>Energy')
    print("<td><input type=checkbox name=industry5 value='health'",end='')
    if health_ind : print('checked', end='')
    print('>Health Care')
    print("<td><input type=checkbox name=industry6 value='tech'",end='')
    if tech : print('checked', end='')
    print('>Technology')
    print("<td><input type=checkbox name=industry7 value='tele'",end='')
    if tele : print('checked', end='')
    print('>Telecom')
    print("<td><input type=checkbox name=industry8 value='mat'",end='')
    if mat : print('checked', end='')
    print('>Material')
    print('</table>')

    print("""
        <br>
        <center>
        <input type=submit value='   Filter   '></center>
        </form>
        <center><table id=table2 border=1>
        <tr>
    """)

    print("<th>Name<th>Age<th>Highest_Education<th>Annual_Income<th>Investment_Goal<th>Security<th>Industry")

    for row in data:
        Fname  = row[0]
        Lname  = row[1]
        Age    = row[2]
        Highest_Education = row[3]
        Annual_Income  = row[4]
        Investment_Objective = row[5]
        Security_Type = row[6]
        Industry_Preference = row[7]

        Name = Fname +' '+ Lname
        Investment_Goal = re.sub(r",", "<br>", Investment_Objective)
        Security  = re.sub(r",",  "<br>", Security_Type)
        Industry = re.sub(r",", "<br>", Industry_Preference)

        print("<tr>", end='')
        print("<td>"+ Name +"<td>"+ Age +"<td>"+ Highest_Education +"<td>"+ Annual_Income +"<td>"+ Investment_Goal +"<td>"+ Security +"<td>"+ Industry, end='')
        print("</tr>")

    print("</table></center><br><br><br><footer>Copyright &copy; TEAM 6</footer>")
    print("</body>")
    print("</html>")


#execute the functions
read_data();
display();

