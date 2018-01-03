#!/usr/bin/env python36


import cgi  # cgi
import cgitb  # cgi with traceback error handling
import pymysql as mydb  # Mysql 3x database driver
import re  # regular expressions

cgitb.enable()

data = []

print("Content-Type: text/html \n")  # required http response header (w/ extra line)




def read_data():
    global sort_field, sort_seq, filter

    elements = cgi.FieldStorage()  # obtain the http parameters

    filter = elements.getvalue('search') or ""
    sort_field = elements.getvalue('sort') or "Fname"
    sort_seq = elements.getvalue('seq') or "asc"

    host = 'localhost'
    port = 3306
    userid = 'team6'
    pswd = 'team6'
    db = 'team6'

    try:
        conn = mydb.connect(host=host, user=userid, password=pswd, database=db)

        cursor = conn.cursor()

        if filter=='':
            sql = "select * from team6_form_data ORDER BY lower(" + sort_field + ") " + sort_seq

        else:
            sql = "SELECT * " \
              + "FROM team6_form_data " \
              + "WHERE Fname  like '%" + filter + "%' " \
              + "   OR Lname   like '%" + filter + "%' " \
              + "   OR Age    like '%" + filter + "%' " \
              + "   OR Gender     like '%" + filter + "%' " \
              + "   OR Highest_Education    like '%" + filter + "%' " \
              + "   OR 	Marital_Status like '%" + filter + "%' " \
              + "   OR Annual_Income   like '%" + filter + "%' " \
              + "   OR Investment_Amount    like '%" + filter + "%' " \
              + "   OR 	Investment_Objective like '%" + filter + "%' " \
              + "   OR Security_Type   like '%" + filter + "%' " \
              + "   OR 	Industry_Preference	 like '%" + filter + "%' " \
              + "   OR Time_Period   like '%" + filter + "%' " \
              + "   OR 	Hypo_Portfolio like '%" + filter + "%' " \
              + "   OR PriceDrop   like '%" + filter + "%' " \
              + "   OR 	PriceSoar	 like '%" + filter + "%' " \
              + "   OR 	Inflation   like '%" + filter + "%' " \
              + "ORDER BY lower(" + sort_field + ") " + sort_seq



        result = cursor.execute(sql);


    except mydb.Error as e:
        errorNum = e.args[0]
        errorMsg = e.args[1]
        error = 'Database Error - ' + str(errorNum) + errorMsg
        return

    i = 0
    row = cursor.fetchone()  # get first row
    while row is not None:
        data.append(row)
        i += 1
        row = cursor.fetchone()  # get next row

    cursor.close()
    conn.close()


#display: display data on the html page



def display():
    global sort_field, sort_seq, filter

    if sort_seq == 'asc':
        sort_seq = 'desc'  # flip the sort seq
    else:
        sort_seq = 'asc'


    print("""
        <html>
        <head>
    <title>Search and Sort_Investment Preference Survey</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" type="text/css" href="survey.css">
        </head>
    <body>
    <header>
    <h1><i class="material-icons">border_color</i>&nbsp;Search and Sort the Survey Results&nbsp;<i class="material-icons">insert_chart</i></h1><br>
    </header>
        <br>
    &nbsp;
    <center><a href='Admin_SearchSortFilter.html'><input type=button value='   Go Back   '></a></center>
    <div class="text">
        <form action=SearchAndSort.py method=GET>
        Search for: <input type=text name=search value= """, end='')
    print("'" + filter + "'", end='')
    print("""
        '> 
        <input type=submit value=search> 
        </form>
        <table border=1>
        <tr>
    """)
    print("<th><a href=SearchAndSort.py?sort=Fname&seq=" + sort_seq + "&search=" + filter + "> Name</a>")
    print("<th><a href=SearchAndSort.py?sort=Age&seq=" + sort_seq + "&search=" + filter + "> Age    </a>")
    print("<th><a href=SearchAndSort.py?sort=Gender&seq=" + sort_seq + "&search=" + filter + "> Gender   </a>")
    print("<th><a href=SearchAndSort.py?sort=Highest_Education&seq=" + sort_seq + "&search=" + filter + "> Highest_Education</a>")
    print("<th><a href=SearchAndSort.py?sort=Marital_Status&seq=" + sort_seq + "&search=" + filter + "> Martial_Status    </a>")
    print("<th><a href=SearchAndSort.py?sort=Annual_Income&seq=" + sort_seq + "&search=" + filter + "> Annual_Income  </a>")
    print("<th><a href=SearchAndSort.py?sort=Investment_Amount&seq=" + sort_seq + "&search=" + filter + "> Investment_Amount  </a>")
    print("<th><a href=SearchAndSort.py?sort=Investment_Objective&seq=" + sort_seq + "&search=" + filter + "> Investment_Objective</a>")
    print("<th><a href=SearchAndSort.py?sort=Security_Type&seq=" + sort_seq + "&search=" + filter + "> Security_Type</a>")
    print("<th><a href=SearchAndSort.py?sort=Industry_Preference&seq=" + sort_seq + "&search=" + filter + "> Industry_Preference </a>")
    print("<th><a href=SearchAndSort.py?sort=Time_Period&seq=" + sort_seq + "&search=" + filter + "> Time_Period    </a>")
    print("<th><a href=SearchAndSort.py?sort=Hypo_Portfolio&seq=" + sort_seq + "&search=" + filter + "> Hypo_Portfolio    </a>")
    print("<th><a href=SearchAndSort.py?sort=PriceDrop&seq=" + sort_seq + "&search=" + filter + "> PriceDrop   </a>")
    print("<th><a href=SearchAndSort.py?sort=PriceSoar&seq=" + sort_seq + "&search=" + filter + "> PriceSoar</a>")
    print("<th><a href=SearchAndSort.py?sort=Inflation&seq=" + sort_seq + "&search=" + filter + "> Inflation</a>")

    for row in data:
        print("<tr>", end='')
        Fname = row[1]
        Lname = row[2]
        Age = row[3]
        Gender = row[4]
        Highest_Education = row[5]
        Marital_Status = row[6]
        Annual_Income = row[7]
        Investment_Amount=row[8]
        Investment_Objective=row[9]
        Security_Type=row[10]
        Industry_Preference=row[11]
        Time_Period=row[12]
        Hypo_Portfolio=row[13]
        PriceDrop=row[14]
        PriceSoar=row[15]
        Inflation=row[16]

        name = Fname + ' ' + Lname
        print("<td>" + name +"</td>")
        print("<td>" + Age + "</td>")
        print("<td>" + Gender+ "</td>")
        print("<td>" + Highest_Education + "</td>")
        print("<td>" + Marital_Status + "</td>")
        print("<td>" + Annual_Income + "</td>")
        print("<td>" + Investment_Amount + "</td>")
        print("<td>" + Investment_Objective + "</td>")
        print("<td>" + Security_Type + "</td>")
        print("<td>" + Industry_Preference + "</td>")
        print("<td>" + Time_Period + "</td>")
        print("<td>" + Hypo_Portfolio + "</td>")
        print("<td>" + PriceDrop + "</td>")
        print("<td>" + PriceSoar + "</td>")
        print("<td>" + Inflation + "</td>")
        print("</tr>")

    print("</table><br><br><br><footer>Copyright &copy; TEAM 6</footer>")
    print("</body>")
    print("</html>")



#call function
read_data();
display();



