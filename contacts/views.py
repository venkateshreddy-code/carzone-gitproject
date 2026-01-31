from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

from .models import Contact

User = get_user_model()


def inquiry(request):
    if request.method != "POST":
        return redirect("/")

    car_id = request.POST.get("car_id", "")
    car_title = request.POST.get("car_title", "")
    first_name = request.POST.get("first_name", "")
    last_name = request.POST.get("last_name", "")
    customer_need = request.POST.get("customer_need", "")
    city = request.POST.get("city", "")
    state = request.POST.get("state", "")
    email = request.POST.get("email", "")
    phone = request.POST.get("phone", "")
    message = request.POST.get("message", "")

    user_id = request.POST.get("user_id")  # might be blank for anonymous users
    if request.user.is_authenticated:
        user_id = request.user.id

        has_contacted = Contact.objects.filter(car_id=car_id, user_id=user_id).exists()
        if has_contacted:
            messages.error(
                request,
                "You have already made an inquiry about this car. Please wait until we get back to you.",
            )
            return redirect("/cars/" + str(car_id))

    contact = Contact(
        car_id=car_id,
        car_title=car_title,
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        customer_need=customer_need,
        city=city,
        state=state,
        email=email,
        phone=phone,
        message=message,
    )
    contact.save()

    admin_emails = list(
        User.objects.filter(is_superuser=True, is_active=True)
        .exclude(email__isnull=True)
        .exclude(email__exact="")
        .values_list("email", flat=True)
    )

    if admin_emails:
        send_mail(
            "New Car Inquiry",
            f"You have a new inquiry for the car {car_title}. Please login to your admin panel for more info.",
            "samsmithss012@gmail.com",
            admin_emails,
            fail_silently=False,
        )

    messages.success(request, "Your request has been submitted, we will get back to you shortly.")
    return redirect("/cars/" + str(car_id))
