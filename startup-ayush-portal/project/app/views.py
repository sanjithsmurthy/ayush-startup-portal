from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'app/index.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Your account has been Successfully Created!")
        return redirect('signin')

    return render(request, 'app/signup.html')

def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'app/home.html', {'fname': fname})

        else:
            messages.error(request, "Bad Credentials!")
            return render(request, 'app/signin.html')
            
    return render(request, 'app/signin.html')


def signout(request):
    pass

def about(request):
    return render(request,'app/about.html')

def home(request):
    return render(request,'app/home.html')

def contact(request):
    return render(request,'app/contact.html')

# def portfolio_view(request):
#     # CONTACT FORM
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         form_data = {
#             'name':name,
#             'email':email,
#             'phone':phone,
#             'message':message,
#         }
#         message = '''
#         From:\n\t\t{}\n
#         Message:\n\t\t{}\n
#         Email:\n\t\t{}\n
#         Phone:\n\t\t{}\n
#         '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['phone'])
#         send_mail('You got a mail!', message, '', ['<your_email>']) # TODO: enter your email address
        
#     return render(request, 'myportfolio/index.html', {})
