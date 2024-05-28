from django.shortcuts import render
from datetime import datetime, timedelta

# #setting/creating/sending cookies view
# def set_cookie(request):
#     res = render(request, 'setcookie.html')
#     # res.set_cookie("name", 'alexa singh', max_age=5)
#     # res.set_cookie("lastName", 'Peter khan', max_age=3)
#     # res.set_cookie("email", 'aman@gmail.com', max_age=10)

#     res.set_cookie("firstname", 'alexa singh', max_age=50)    
#     res.set_cookie("lastName", 'Peter khan', max_age=30)
#     res.set_cookie("email", 'aman@gmail.com', max_age=100)
#     res.set_cookie('name', "Ankita singh",  expires=datetime.utcnow()+timedelta(days=2))
#     return res

# #getting  cookies view
# def get_cookie(request):    
#     # firstName = request.COOKIES['name']
#     # lastName = request.COOKIES['lastName']
#     # email = request.COOKIES['email']
#     firstName = request.COOKIES.get("firstname", "Name is not alive")
#     lastName = request.COOKIES.get("lastName", 'Last Name is not alive')
#     email = request.COOKIES.get("email", "email is not alive")
#     detail = {
#         "firstname" : firstName,
#         'lastName' : lastName,
#         'email' : email
#     }
#     return render(request, 'getcookie.html', context=detail)

# #delete cookie view
# def delcookies(request):
#     res = render(request, 'delcookie.html')
#     res.delete_cookie('firstname')
#     res.delete_cookie('lastName')
#     res.delete_cookie('email')
#     return res



#setting/creating/sending cookies view
# def set_signed_cookie(request):
#     res = render(request, 'setcookie.html')
#     res.set_signed_cookie("address", 'Noida sector 189', salt="useraddress")
#     res.set_signed_cookie("color", 'Blue', max_age=10)
#     res.set_signed_cookie("email", 'aman@gmail.com', max_age=10)
#     res.set_signed_cookie('name', "Ankita singh",  expires=datetime.utcnow()+timedelta(days=2), salt="securecookie")
#     return res

# #getting signed cookies view
# def get_signed_cookie(request):    
#     address = request.get_signed_cookie('address', 'Not Found', salt="useraddress")
#     color = request.get_signed_cookie('color', 'Not Found')
#     email = request.get_signed_cookie('email', 'Not Found')
#     name = request.get_signed_cookie('name', 'Not Found', salt="securecookie")
#     detail = {
#         "address" : address,
#         'color' : color,
#         'email' : email,
#         'name' : name,
#     }
#     return render(request, 'getcookie.html', context=detail)


#delete signed  cookie view - do yourself
# def delcookies(request):
#     res = render(request, 'delcookie.html')
#     res.delete_cookie('firstname')
#     res.delete_cookie('lastName')
#     res.delete_cookie('email')
#     return res



#setting session view
def set_session(request):
    request.session['first_name'] = "Robinson"
    request.session['last_name'] = "Singh"
    request.session['address'] = "Pune"
    return render(request ,'session/setsession.html')
#setting session view
def get_session(request):
    fname = request.session['first_name']
    lname = request.session['last_name']
    address = request.session['address']
    # fname = request.session.get('first_name', "Not Available")
    # lname = request.session.get('last_name', "Not Available")
    # address = request.session.get('address', "Not Available")
    detail  = {
        'fn': fname,
        'ln' : lname,
        'add' : address
    } 
    request.session.clear()
    request.session.setdefault(key="first_name", value="NA")
    request.session.setdefault(key="last_name", value="Na")
    request.session.setdefault(key="address", value="Na ")
    print(request.session.keys())
    print(request.session.values())
    print(dict(request.session.items()))
    return render(request ,'session/getsession.html', context=detail)

#setting session view
def del_session(request):
    return render(request ,'session/delsession.html')