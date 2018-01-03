#!/usr/bin/env python36

import cgi
import cgitb
import CookieFunction                 #import cookie functions


cgitb.enable()              #activate the cgi traceback error handling

print("Content-Type: text/html")


firstname = CookieFunction.getCookie('firstname');
lastname = CookieFunction.getCookie('lastname');
age = CookieFunction.getCookie('age');
gender = CookieFunction.getCookie('gender');
education = CookieFunction.getCookie('education');
marriage = CookieFunction.getCookie('marriage');
income = CookieFunction.getCookie('income');

investAmount = CookieFunction.getCookie('investAmount');
objective = CookieFunction.getCookie('objective');
security = CookieFunction.getCookie('security');
industry = CookieFunction.getCookie('industry');
time = CookieFunction.getCookie('time');

hypo_port = CookieFunction.getCookie('hypo_port');
price_drop = CookieFunction.getCookie('price_drop');
price_soar = CookieFunction.getCookie('price_soar');
inflation = CookieFunction.getCookie('inflation');


#define display() function
def display():
    print("""
    <html>
<head>
    <title>Review Your Response</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" type="text/css" href="survey.css">
    <style>
        button{
        border: none;
        background-color: rgb(229,167,42);
        color: darkslategrey;
        padding: 10px;
        border-radius: 10px;
        font-family: "Helvetica Neue";
        font-size: 28pt;
        font-weight: bold;
        }
        body{
        background-color: white;
        }
        h1{
        color: darkgreen;
        }
    </style>
    </head>
<body>
<header>   
    <center>
            <h1 style="color: white"><i class="material-icons">	border_color</i>&nbsp;Review Your Response&nbsp;<i class="material-icons">		insert_chart</i></h1>
        </center>
    </header>
<div>
    """)
    print("<form method=post name=review action=" + __file__ + ">")
    print("""
    <center>
        <h1>Please Review Your Reponse</h1>
        <table style="color:darkgreen" border=1>
    """)
    print("<tr><td>First Name</td><td>" + firstname + "</td></tr>")
    print("<tr><td>Last Name</td><td>" + lastname + "</td></tr>")
    print("<tr><td>Age</td><td>" + age + "</td></tr>")
    print("<tr><td>Gender</td><td>" + gender + "</td></tr>")
    print("<tr><td>Education</td><td>" + education + "</td></tr>")
    print("<tr><td>Martial Status</td><td>" + marriage + "</td></tr>")
    print("<tr><td>Income</td><td>" + income + "</td></tr>")
    print("<tr><td>Invest Amount</td><td>" + investAmount + "</td></tr>")
    print("<tr><td>Objective</td><td>" + objective + "</td></tr>")
    print("<tr><td>Security</td><td>" + security + "</td></tr>")
    print("<tr><td>Industry</td><td>" + industry + "</td></tr>")
    print("<tr><td>Length</td><td>" + time + "</td></tr>")
    print("<tr><td>Hypo_Porfolio</td><td>" + hypo_port + "</td></tr>")
    print("<tr><td>Price Drop</td><td>" + price_drop + "</td></tr>")
    print("<tr><td>Price Soar</td><td>" + price_soar + "</td></tr>")
    print("<tr><td>Inflation</td><td>" + inflation + "</td></tr>")
    print("""
    </table>
    </center>
    </form>
    </div>
    

<center>
<table>
    <tr></tr>
    <tr></tr>
    <tr></tr>
    <tr>
        <td><center><a href="page1.py"><input type=Reset value="Clear All"></a></center></td>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
        <td><center><input type=submit value=Submit onclick="window.location.href='saveDBandRecommend.py'"></center></td>
    
    </table> 
    <br>

    </center>  
    <footer>Copyright &copy; TEAM 6</footer>   
</body>
</html>
    """)


# call function

display()
