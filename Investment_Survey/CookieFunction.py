

def setCookie(name, value, expire=0):
    from http import cookies
    c = cookies.SimpleCookie()  
    c[name] = value  
    if int(expire) != 0:
        maxAge = int(expire) * (24 * 60 * 60) 
        c[name]['max-age'] = maxAge  
    c[name]['path'] = '/'  
    print(c.output())  


 
def getCookies():
    import os, urllib

    cookiesDict = {}  
    allCookies = os.environ.get('HTTP_COOKIE') 
    
    if allCookies is None: return

    cookiesArray = allCookies.split('; ')
    for cookie in cookiesArray:
        (name, value) = cookie.split('=', 1)  
        value2 = urllib.parse.unquote(value) 
        cookiesDict[name] = value2  
    return cookiesDict


def getCookie(name):
    cookies = getCookies()
    try:
        value = cookies[name]  
    except:
        value = ''  
    return value

