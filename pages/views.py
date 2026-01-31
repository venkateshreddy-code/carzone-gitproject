from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages






def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')[:6]   # or '-id' if you don’t have created_date
    search_fields = Car.objects.values('model', 'city' , 'year','body_style')
    data = {
     'teams': teams,
     'featured_cars':featured_cars,
     'all_cars':all_cars,
     'search_fields':search_fields,
    }

    return render(request, "pages/home.html", data)


def about(request):
    teams = Team.objects.all()

    return render(request, 'pages/about.html', {"teams": teams})

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        phone = request.POST.get("phone", "").strip()
        message_text = request.POST.get("message", "").strip()

        email_subject = f"You have a new message from Carzone website regarding {subject}"
        message_body = (
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n"
            f"Message: {message_text}\n"
        )

        # Get ALL superuser emails (handles multiple superusers safely)
        admin_emails = list(
            User.objects.filter(is_superuser=True)
            .exclude(email__isnull=True)
            .exclude(email__exact="")
            .values_list("email", flat=True)
        )

        if admin_emails:
            send_mail(
                subject=email_subject,
                message=message_body,
                from_email="samsmithss012@gmail.com",   # can keep this for now
                recipient_list=admin_emails,
                fail_silently=False,
            )

        messages.success(request, "Thank you for contacting us. We will get back to you shortly.")
        return redirect("contact")

    return render(request, "pages/contact.html")

def cars(request):
    return render(request, 'pages/cars.html')
