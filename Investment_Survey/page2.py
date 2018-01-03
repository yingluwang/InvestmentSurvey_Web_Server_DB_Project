#!/usr/bin/env python36

import cgi
import cgitb
import CookieFunction                 #import cookie functions

cgitb.enable()              #activate the cgi traceback error handling
print("Content-Type: text/html")


#obtain user cookie
firstname = CookieFunction.getCookie('firstname');
lastname = CookieFunction.getCookie('lastname');
age = CookieFunction.getCookie('age');
gender = CookieFunction.getCookie('gender');
education = CookieFunction.getCookie('education');
marriage = CookieFunction.getCookie('marriage');
income = CookieFunction.getCookie('income');


elements = cgi.FieldStorage()

#page2 info
investAmount=elements.getvalue('investAmount') or ""

#checkbox-investment objective
objective1=elements.getvalue('objective1') or ""
objective2=elements.getvalue('objective2') or ""
objective3=elements.getvalue('objective3') or ""
objective4=elements.getvalue('objective4') or ""

#checkbox-type of securities
security1=elements.getvalue('security1') or ""
security2=elements.getvalue('security2') or ""
security3=elements.getvalue('security3') or ""


#checkbox-type of industry
industry1=elements.getvalue('industry1') or ""
industry2=elements.getvalue('industry2') or ""
industry3=elements.getvalue('industry3') or ""
industry4=elements.getvalue('industry4') or ""
industry5=elements.getvalue('industry5') or ""
industry6=elements.getvalue('industry6') or ""
industry7=elements.getvalue('industry7') or ""
industry8=elements.getvalue('industry8') or ""

time=elements.getvalue("time") or ""


objective=''
security=''
industry=''
msg=''

def checkbox_concat():

    global objective
    global security
    global industry


    if objective1==''and objective2=='' and objective3=='' and objective4=='':
        objective=''
    else:
        if objective1: objective += objective1+','
        if objective2: objective += objective2 + ','
        if objective3: objective += objective3 + ','
        if objective4: objective += objective4 + ','

    if security1=='' and security2=='' and security3=='':
        security==''
    else:
        if security1: security += security1+','
        if security2: security += security2+','
        if security3: security += security3+','

    if industry1=='' and industry2=='' and industry3=='' and industry4=='' and industry5=='' and industry6=='' and industry7==''and industry8=='':
        industry==''
    else:
        if industry1: industry += industry1 + ','
        if industry2: industry += industry2 + ','
        if industry3: industry += industry3 + ','
        if industry4: industry += industry4 + ','
        if industry5: industry += industry5 + ','
        if industry6: industry += industry6 + ','
        if industry7: industry += industry7 + ','
        if industry8: industry += industry8

# function to check people fill in the multi-value questions
def validate():
    global msg
    global investAmount
    global time
    if investAmount=="":
        msg = 'Please choose your investment amount'
    if time == "":
        msg = 'Please choose your length of investment'
    if industry=='':
        msg='Please choose industry you like'
    if objective=='':
        msg='Please choose your investment objective'
    if security=='':
        msg='Please choose the security type you like'

#save cookies
def save_cookie():
    #save temporarily
    print('Set-Cookie: investAmount=' + investAmount + '; path=/')  # temporary
    print('Set-Cookie: objective=' + objective + '; path=/')
    print('Set-Cookie: security=' + security + '; path=/')
    print('Set-Cookie: industry=' + industry + '; path=/')
    print('Set-Cookie: time=' + time + '; path=/')


# to display survey page2
def display():
    print("""
        <html>
        <head>
        <title>Investment Preference Survey_2</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
        <link rel="stylesheet" type="text/css" href="survey.css">
        </head>
        <body>
        <header>
        <center>
        <h1><i class="material-icons">	border_color</i>&nbsp;INVESTMENT PREFERENCE SURVEY&nbsp;<i class="material-icons">		insert_chart</i></h1>
        </center></header>
        <br>
        <br>
        <div id="progressbar">
        <div style="background-color: rgb(229,167,42);
        width: 60%;  height: 20px;border-radius: 10px;display: block;"><center >60%</center></div>
        </div>
        <div class="text">
    """)
    print("<form method=post name=page2 action=" + __file__ + ">")
    print("""
<fieldset>
    """)
    print('<b>What is your investment amount (US dollars)? </b><br>')  # radio button
    print('<input type="radio" name="investAmount" value="<5000" ', end='')
    if investAmount == '<5000': print('checked', end='')
    print('>   5,000')
    print('<input type="radio" name="investAmount" value="5000-10000" ', end='')
    if investAmount == '5000-10000': print('checked', end='')
    print('>5,000-10,000')
    print('<input type="radio" name="investAmount" value="10000-20000" ', end='')
    if investAmount == '10000-20000': print('checked', end='')
    print('> 10,000-20,000')
    print('<input type="radio" name="investAmount" value=">20000" ', end='')
    if investAmount == '>20000': print('checked', end='')
    print('> >20,000')



    print('<br><br><b>Please select your investment objective? (Can choose more than one) </b><br>')
    print('<input type="checkbox" name="objective1" value="Goal" ', end='')
    if objective1 != '': print('checked', end='')
    print('> Financial goal')
    print('<input type="checkbox" name="objective2" value="edu" ', end='')
    if objective2 != '': print('checked', end='')
    print('> educations')
    print('<input type="checkbox" name="objective3" value="retirement" ', end='')
    if objective3!= '': print('checked', end='')
    print('> retirement')
    print('<input type="checkbox" name="objective4" value="health" ', end='')
    if objective4!= '': print('checked', end='')
    print('> Healthcare')

    print('<br><br><b>What type of securities do you want to include in your portfolio? (Can choose more than one) </b><br>')
    print('<input type="checkbox" name="security1" value="debt" ', end='')
    if security1 != '': print('checked', end='')
    print('> Debt')
    print('<input type="checkbox" name="security2" value="equity" ', end='')
    if security2 != '': print('checked', end='')
    print('> Equity')
    print('<input type="checkbox" name="security3" value="derivative" ', end='')
    if security3 != '': print('checked', end='')
    print('> Derivative')

    print('<br><br><b>What industries do you prefer?(Can choose more than one) </b><br>')
    print('<input type="checkbox" name="industry1" value="fin" ', end='')
    if industry1 != '': print('checked', end='')
    print('> Financial')
    print('<input type="checkbox" name="industry2" value="uti" ', end='')
    if industry2 != '': print('checked', end='')
    print('>Utility')
    print('<input type="checkbox" name="industry3" value="consume" ', end='')
    if industry3 != '': print('checked', end='')
    print('> Consumer')
    print('<input type="checkbox" name="industry4" value="ene" ', end='')
    if industry4 != '': print('checked', end='')
    print('> Energy')
    print('<input type="checkbox" name="industry5" value="health" ', end='')
    if industry5 != '': print('checked', end='')
    print('> HealthCare')
    print('<input type="checkbox" name="industry6" value="tech" ', end='')
    if industry6 != '': print('checked', end='')
    print('> Technology')
    print('<input type="checkbox" name="industry7" value="tele" ', end='')
    if industry7 != '': print('checked', end='')
    print('> Telcom')
    print('<input type="checkbox" name="industry8" value="mat" ', end='')
    if industry8 != '': print('checked', end='')
    print('> Materials')

    print('<br><br><b>How long do you plan to keep your portfolio? </b><br>')  # radio button
    print('<input type="radio" name="time" value="1m" ', end='')
    if time == '1m': print('checked', end='')
    print('>   One Month')
    print('<input type="radio" name="time" value="1-3" ', end='')
    if time == '1-3': print('checked', end='')
    print('>One-Three Months')
    print('<input type="radio" name="time" value="6" ', end='')
    if time == '6': print('checked', end='')
    print('> Half an Year')
    print('<input type="radio" name="time" value="1y" ', end='')
    if time == '1y': print('checked', end='')
    print('> One Year')
    print('<input type="radio" name="time" value="1-2y" ', end='')
    if time == '1-2y': print('checked', end='')
    print('>One-Two Years')
    print('<input type="radio" name="time" value="2-5y" ', end='')
    if time == '2-5y': print('checked', end='')
    print('> Two-Five Years')
    print('<input type="radio" name="time" value="5" ', end='')
    if time== '5': print('checked', end='')
    print('> More than 5 Ysears')



    print("""
        </fieldset>
        </center>
    """)
    print("""
        <center>
        <table>
        <tr></tr>
        <tr></tr>
        <tr></tr>
        <tr>
        <td><center><input type=submit value=Next></center></td>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
        <td><center><input type=Reset value=Clear></center></td>
    """)
    print("<center><p style='color:red'>" + msg + '</p></center>')
    print("""

        </table>
        </form>
        </div>
    """)





# call function

if elements:
    checkbox_concat()
    validate()
    if msg=='':
        save_cookie()
        print("Location: /~wangy/investment_survey/page3.py")  # redirect to another page
        print("\n") #must have this new space

display()
