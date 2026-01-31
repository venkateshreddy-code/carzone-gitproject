from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required



def login(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()

        if not email or not password:
            messages.error(request, "Please enter both email and password.")
            return redirect("login")

        user_obj = User.objects.filter(email__iexact=email).first()
        if user_obj is None:
            messages.error(request, "Invalid login credentials")
            return redirect("login")

        user = auth.authenticate(username=user_obj.username, password=password)
        if user is None:
            messages.error(request, "Invalid login credentials")
            return redirect("login")

        auth.login(request, user)
        messages.success(request, "You are now logged in.")
        return redirect("dashboard")

    return render(request, "accounts/login.html")



def register(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname", "").strip()
        lastname = request.POST.get("lastname", "").strip()
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=firstname,
            last_name=lastname,
        )
        user.save()

        auth.login(request, user)
        messages.success(request, "You are now logged in.")
        return redirect("dashboard")

    return render(request, "accounts/register.html")


@login_required(login_url = 'login')
def dashboard(request):
    user_inquiry = Contact.objects.filter(user_id=request.user.id).order_by('-create_date')

    data = {
        "inquiries" : user_inquiry,
    }

    return render(request, "accounts/dashboard.html", data)


def logout(request):
    if request.method == "POST":
        auth.logout(request)

        return redirect("home")
    return redirect("home")
