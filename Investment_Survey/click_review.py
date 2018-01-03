#!/usr/bin/env python36

import cgi
import cgitb


cgitb.enable()  # activate the cgi traceback error handling

print("Content-Type: text/html")



# define display() function
def display():
    print("""
    <html>
<head>
    <title>Transitioning</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" type="text/css" href="survey.css">
    </head>
<body>
<header>   
    <center>
            <h1 style="color: white"><i class="material-icons">	border_color</i>&nbsp;Transitioning &nbsp;<i class="material-icons">		insert_chart</i></h1>
        </center>
    </header>
<div>
    """)
    print("""
    <br>
    <br>
    <br>
    <br>
    <br>
    <center><a href='review.py'><input type=button value='   Click to Review Your Response   '></a></center>
    <div class="text"></center>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <footer>Copyright &copy; TEAM 6</footer>   
</body>
</html>
    """)


# call function

display()
