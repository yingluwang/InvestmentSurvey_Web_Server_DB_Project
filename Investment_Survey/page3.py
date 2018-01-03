#!/usr/bin/env python36

import cgi
import cgitb
import CookieFunction                 #import cookie functions

cgitb.enable()
print("Content-Type: text/html")
elements = cgi.FieldStorage()

# obtain user cookie
#page1 info
firstname = CookieFunction.getCookie('firstname');
lastname = CookieFunction.getCookie('lastname');
age = CookieFunction.getCookie('age');
gender = CookieFunction.getCookie('gender');
education = CookieFunction.getCookie('education');
marriage = CookieFunction.getCookie('marriage');
income = CookieFunction.getCookie('income');
# obtain user cookie
#page2info
investAmount = CookieFunction.getCookie('investAmount');
objective = CookieFunction.getCookie('objective');
security = CookieFunction.getCookie('security');
industry = CookieFunction.getCookie('industry');
time = CookieFunction.getCookie('time');





# page3 info
hypo_port = elements.getvalue('HypotheticalPortfolio')
price_drop=elements.getvalue('PriceDrop')
price_soar=elements.getvalue('PriceSoar')
inflation=elements.getvalue('InflationRate')


# Function to save cookie page3
def save_cookie():
    # save temporarily
    print('Set-Cookie: hypo_port=' + hypo_port + '; path=/')  # temporary
    print('Set-Cookie: price_drop=' + price_drop + '; path=/')
    print('Set-Cookie: price_soar=' + price_soar + '; path=/')
    print('Set-Cookie: inflation=' + inflation + '; path=/')



# display the page3
def display():
    print("""
        <html>
    <head>
    <title>Investment Preference Survey_3</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" type="text/css" href="survey.css">
    </head>
    <body>
    <header>
    <center>
        <h1><i class="material-icons">	border_color</i>&nbsp;INVESTMENT PREFERENCE SURVEY&nbsp;<i class="material-icons">		insert_chart</i></h1>
    </center>
</header>
<br>
<br>
<div id="progressbar">
  <div style="background-color: rgb(229,167,42);
   width: 90%;  height: 20px;border-radius: 10px;display: block;"><center >90%</center></div>
</div>
<div class="text">
    """)
    print("<form method=post name=page3 action=" + __file__ + ">")
    print("""
        <center>
<fieldset>
<table>

	<tr><td colspan = 5><b>If you could choose only one of the five hypothetical portfolios characterized below, which would you select?</b></td></tr>
	<tr></tr>
    <tr><td></td><td colspan="3"><img src="page_picture/page3.png"></td><td></td></tr>
	<tr>
	<td><input required type=radio  name =HypotheticalPortfolio  value='A'> Portfolio A</td>
    <td><input type=radio  name = HypotheticalPortfolio  value='B'> Portfolio B</td>
    <td><input type=radio  name = HypotheticalPortfolio  value='C' /> Portfolio C</td>
    <td><input type=radio  name = HypotheticalPortfolio value='D' /> Portfolio D</td>
	<td><input type=radio  name = HypotheticalPortfolio  value='E' /> Portfolio E</td>
	</tr>
	<tr></tr><tr></tr><tr></tr>

	<tr><td colspan =5><b>If your owned stock drops 30% in three months,  what would you do?</b></td></tr>
	<tr>
	<td><input requried type=radio  name = PriceDrop id =1 value='A' /> <label for = '1'>Sell all of your stocks</label>
	</td>
    <td><input type=radio  name = PriceDrop id = 2  value='B' /> <label for = '2'>Sell portion of your stocks</label>
    </td>
    <td><input type=radio  name = PriceDrop id = 3  value='C' /> <label for = '3'> Hold all the the stock</label>
    </td>
    <td><input type="radio"  name = PriceDrop id = 4 value='D' /> <label for = "4"> Buy all of the stock</label>
    </td>
	</tr>
	<tr></tr><tr></tr><tr></tr>

	<tr><td colspan =5><b>If your owned stock soars 40% in three months, what would you do?</b></td></tr>
	<tr>
	<td><input required type="radio"  name = PriceSoar value='A' /> Sell all of your stocks</td>
    <td><input type="radio"  name = PriceSoar value='B' /> Sell portion of your stocks</td>
    <td><input type="radio"  name = PriceSoar value='C' /> Hold all the the stock</td>
    <td><input type="radio"  name = PriceSoar value='D' /> Buy all of the stock</td>
	</tr>
	<tr></tr><tr></tr><tr></tr>


	<tr><td colspan =5><b>Extremely conservative investments sometimes earn less than the inflation rate. This may result in the loss of purchasing power. With respect to your investment objectives, which of the following is most true?</b></td></tr>
	<tr>
        <td colspan =5><input required type=radio  name = InflationRate  value='A' /> My investments should be safe, even if it means my returns do not keep pace with inflation.</td></tr>
    <tr>
        <td colspan =5><input type="radio"  name = InflationRate  value='B' /> I am willing to risk an occasional loss of investment value so that my investments may grow at about the same rate as inflation over time.</td></tr>
    <tr><td colspan =5><input type="radio"  name = InflationRate  value='C' /> It is important that my investments grow somewhat faster than inflation. I am willing to accept some risk to achieve this goal.</td></tr>
    <tr>
        <td colspan =5><input type="radio"  name = InflationRate  value='D' /> My investments should grow much faster than inflation. I am willing to accept considerable risk to achieve this goal.</td></tr>
	<tr></tr>

<tr></tr>

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
    print("Location: /~wangy/investment_survey/click_review.py")  # redirect to review page for user's review
    print("\n")

display()
