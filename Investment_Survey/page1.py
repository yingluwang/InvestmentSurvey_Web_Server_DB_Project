#!/usr/bin/env python36

import cgi
import cgitb

cgitb.enable()

print("Content-Type: text/html")

elements = cgi.FieldStorage()

# page1 info
firstname=elements.getvalue('fname')
lastname=elements.getvalue('lname')
age=elements.getvalue('age')
gender=elements.getvalue('gender')
education=elements.getvalue('edu')
marriage=elements.getvalue('marriage')
income=elements.getvalue('income')


msg = ''


# save cookies
def save_cookie():

    print('Set-Cookie: firstname=' + firstname + '; path=/')  # temporary
    print('Set-Cookie: lastname=' + lastname + '; path=/')
    print('Set-Cookie: age=' + age + '; path=/')
    print('Set-Cookie: gender =' + gender + '; path=/')
    print('Set-Cookie: education =' + education + '; path=/')
    print('Set-Cookie: marriage=' + marriage + '; path=/')
    print('Set-Cookie: income =' + income + '; path=/')



# display the survey
def display():
    print("""
        <html>
        <head>
    <title>Investment Preference Survey_1</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" type="text/css" href="survey.css">
        </head>
    <body>
    <header>
    <h1><i class="material-icons">border_color</i>&nbsp;CUSTOMER PROFILE&nbsp;<i class="material-icons">insert_chart</i></h1><br>
    </header>
        <br>
    <div id="progressbar">
    <div style="background-color: rgb(229,167,42);
   width: 30%;  height: 20px;border-radius: 10px;display: block;"><center>30%</center></div>
    </div>
    &nbsp;
    <div class="text">
    """)
    print("<form method=post name=page1 action=" + __file__ + ">")
    print("""
        <center>
<fieldset>
    <table>
      <tr>
        <td style="font-weight: bold">First Name</td>
        <td><input required type="text" name="fname" id="fname" size="20" style="padding: 3px;background-color: white;"></td>
      </tr>
      <tr></tr><tr></tr><tr></tr>
      <tr>
        <td style="font-weight: bold">Last Name</td>
        <td><input required type="text" name="lname" id="lname" size="20" style="font-weight: bold;padding: 3px;background-color: white;"></td>
      </tr>
      <tr></tr><tr></tr><tr></tr>
      <tr>
        <td style="font-weight: bold">Age</td>
        <td>
        <select required name="age" id="age" class="input">
          <option id="default" value=0>--Choose from below--</option>
          <option id="first" value=1>18~22</option>
          <option id="second" value=2>23~27</option>
          <option id="third" value=3>28~32</option>
          <option id="fourth" value=4>33~37</option>
          <option id="fifth" value=5>38~42</option>
          <option id="sixth" value=6>43~47</option>
          <option id="seventh" value=7>48~52</option>
            <option id="eighth" value=8>>52</option></select>
        </td>
      </tr><tr></tr><tr></tr><tr></tr>
      <tr>
        <td style="font-weight: bold">Gender</td>
        <td>
          <input required type="radio" name="gender" id="Male" value='M'>
          <label>Male</label>
          <input type="radio" name="gender" id="Female" value='F'>
          <label>Female</label>
        </td>
      </tr><tr></tr><tr></tr><tr></tr>
      <tr>
        <td style="font-weight: bold">Highest Education</td>
        <td>
        <select required name="edu" id="slctSingle" class="input">
          <option id="default" value=0>--Choose from below--</option>
          <option id="HS" value="HS">High School</option>
          <option id="B" value="B">Bachelor's Degree</option>
          <option id="M" value="M">Master's Degree</option>
          <option id="PhD" value="PhD">PhD</option>
        </select>
        </td>
      </tr><tr></tr><tr></tr><tr></tr>
      <tr>
        <td style="font-weight: bold">Marital Status</td>
        <td>
          <input required type="radio" name="marriage" id="single" value='s'>
          <label>Single</label>
          <input type="radio" name="marriage" id="married" value='m'>
          <label>Married</label>
          <input type="radio" name="marriage" id="divorced" value='d'>
          <label>Divorced</label>
          <input type="radio" name="marriage" id="widowed" value='w'>
          <label>Widowed</label>
          <input type="radio" name="marriage" id="s_d" value='sd'>
          <label>Single with dependent</label>
          <input type="radio" name="marriage" id="m_d" value='md'>
          <label>Married with dependent</label>
        </td>
      </tr><tr></tr><tr></tr><tr></tr>
      <tr>
        <td style="font-weight: bold">Annual Income</td>
        <td>
        <select required name="income" id="income" class="input">
          <option id="default" value=0>--Not include the upper limit for each range--</option>
          <option id="first" value='1'>Below 20K</option>
          <option id="second" value='2'>20K~75K</option>
          <option id="third" value='3'>75K~90K</option>
          <option id="fourth" value='4'>90K~200K</option>
          <option id="fifth" value='5'>200K~400K</option>
            <option id="sixth" value='6'>Above 400K</option></select></td>
      </tr>
    </table>
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
</table>
</center>

</form>
</div>

<footer>Copyright &copy; TEAM 6</footer>

</body>
</html>
    """)


# call function
if elements:
    save_cookie()
    print("Location: /~wangy/investment_survey/page2.py")  # redirect to page2  #absolute path 
    print("\n")

display()
