from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
# from .forms import CustomLoginForm, CustomRegistrationForm

User = get_user_model()

# Home View
def home_view(request):
    return render(request, 'home.html') 

# Login View using Forms.py
# def login_view(request):
#     if request.method == 'POST':
#         form = CustomLoginForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             print(user)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = CustomLoginForm()
#     return render(request, 'login.html', {'form': form})

# Login View
def login_view(request):    
    error = None
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if "@" in username:
            try:
                user_obj = User.objects.get(email = username)
                username = user_obj.username
            except User.DoesNotExist:
                error = "Invalid credentials"
                return render(request, "login.html", {"error": error})

        print(len(username))
        print(len(password))
        user = authenticate(username=username, password=password)
        # print(User.objects.all())
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, 'login.html')

# Register View
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')

    return render(request, 'register.html')


# Register view from custom model
# def register_view(request):
#     if request.method == 'POST':
#         form = CustomRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = CustomRegistrationForm()
    
#     return render(request, 'register.html', {'form': form})