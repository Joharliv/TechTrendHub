from django.shortcuts import render , redirect
from .models import User
from django.contrib.auth import authenticate, login as auth_login


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def cart(request): 
    return render(request, 'cart.html')

def product(request):
    return render(request, 'product.html')

def product2(request):
    return render(request, 'product2.html')

def product3(request):
    return render(request, 'product3.html')

def product4(request):  
    return render(request, 'product4.html')

def product5(request):
    return render(request, 'product5.html')

def product6(request):  
    return render(request, 'product6.html')

def product7(request):
    return render(request, 'product7.html')

def product8(request):
    return render(request, 'product8.html')

def product9(request):  
    return render(request, 'product9.html')

def product10(request):
    return render(request, 'product10.html')

def product11(request):
    return render(request, 'product11.html')

def product12(request):
    return render(request, 'product12.html')

def product13(request):
    return render(request, 'product13.html')

def product14(request):
    return render(request, 'product14.html')

def product15(request):
    return render(request, 'product15.html')

def product16(request):
    return render(request, 'product16.html')

def product17(request):
    return render(request, 'product17.html')

def product18(request):
    return render(request, 'product18.html')

def product19(request):
    return render(request, 'product19.html')

def shop(request):
    return render(request, 'shop.html')

def buy(request):
    return render(request, 'buy.html')

def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirmPassword")

        if not mobile.isdigit() or len(mobile) != 10:
            return render(request, 'signup.html', {'error': "Mobile number must be exactly 10 digits."})

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': "Username already exists. Please choose another."})

        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': "Email already exists. Please use another."})

        if password != confirm_password:
            return render(request, 'signup.html', {'error': "Passwords do not match."})

        user = User(name=name, username=username, mobile=mobile, email=email, password=password)
        user.save()

        return redirect('login')

    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if the user exists
        user = User.objects.filter(username=username).first()

        if user:
            # Check if password matches
            if user.password == password:
                # Log the user in (note: for security, Django provides a more secure method)
                request.session['username'] = username  # store username in session
                return redirect('shop')  # Redirect to the home page (create a view for it)
            else:
                return render(request, 'login.html', {'error': 'Incorrect password.'})
        else:
            return render(request, 'login.html', {'error': 'Username not found. Please sign up.'})

    return render(request, 'login.html')


