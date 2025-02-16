from django.shortcuts import render, redirect
from .models import Customers
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import authentication, login
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth import logout
# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name', '') #default empty
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        birth_date = request.POST.get('birth_date', '') #default empty
        
        #new customer instance
        customer = Customers(
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
            email = email,
            password = make_password(password),
            birth_date = birth_date
        )
        customer.save()
        messages.success(request, 'Success register')
        return redirect('login')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = Customers.objects.get(email = email)
            if check_password(password, user.password):
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid email or password')
        except Customers.DoesNotExist:
            messages.error(request, 'User not found')
    return render(request, 'login.html')
#user profile
@login_required

def profile(request):
    user = request.user
    
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.phone_number = request.POST.get('phone_number', user.phone_number)
        user.birth_date = request.POST.get('birth_date', user.birth_date)
        user.save()
        messages.success(request, 'Profile updated successfully!')
    
    return render(request, 'profile.html', {'user': user})

#send message


@login_required
def send_message(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        
        # Create a new message instance
        message = Message(description=description, user=request.user)
        message.save()
        messages.success(request, 'Message sent successfully!')
        return redirect('profile')  # Redirect to profile or wherever desired
    
    return render(request, 'send_message.html')
#view message
@login_required
def view_messages(request):
    messages = Message.objects.filter(user=request.user)  # Get messages for the logged-in user
    return render(request, 'view_messages.html', {'messages': messages})

#logout



def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout