from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Car


def cars(request):
    cars_list = Car.objects.order_by("-created_date")
    paginator = Paginator(cars_list, 4)
    page = request.GET.get("page")
    paged_cars = paginator.get_page(page)

    models = Car.objects.values_list("model", flat=True).exclude(model__isnull=True).exclude(model__exact="").distinct().order_by("model")
    cities = Car.objects.values_list("city", flat=True).exclude(city__isnull=True).exclude(city__exact="").distinct().order_by("city")
    years = Car.objects.values_list("year", flat=True).exclude(year__isnull=True).distinct().order_by("year")
    body_styles = Car.objects.values_list("body_style", flat=True).exclude(body_style__isnull=True).exclude(body_style__exact="").distinct().order_by("body_style")
    transmissions = Car.objects.values_list("transmission", flat=True).exclude(transmission__isnull=True).exclude(transmission__exact="").distinct().order_by("transmission")

    return render(request, "cars/cars.html", {
        "cars": paged_cars,
        "models": models,
        "cities": cities,
        "years": years,
        "body_styles": body_styles,
        "transmissions": transmissions,
    })


def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    return render(request, "cars/car_detail.html", {"single_car": single_car})


def search(request, keyword=None):
    q_text = (
        keyword
        or request.GET.get("q", "")
        or request.GET.get("keyword", "")
    ).strip()

    cars = Car.objects.order_by("-created_date")

    model = (request.GET.get("select-make") or "").strip()
    city = (request.GET.get("select-location") or "").strip()
    year = (request.GET.get("select-year") or "").strip()
    body_style = (request.GET.get("select-type") or "").strip()
    transmission = (request.GET.get("transmission") or "").strip()
    min_price = (request.GET.get("min_price") or "").strip()
    max_price = (request.GET.get("max_price") or "").strip()

    # keyword search
    if q_text:
        cars = cars.filter(
            Q(car_title__icontains=q_text) |
            Q(description__icontains=q_text) |
            Q(model__icontains=q_text) |
            Q(city__icontains=q_text) |
            Q(state__icontains=q_text) |
            Q(body_style__icontains=q_text) |
            Q(transmission__icontains=q_text)
        )

    # dropdown filters
    if model:
        cars = cars.filter(model__icontains=model)

    if city:
        cars = cars.filter(city__icontains=city)

    if year:
        cars = cars.filter(year=year)

    if body_style:
        cars = cars.filter(body_style__icontains=body_style)

    if transmission:
        cars = cars.filter(transmission__icontains=transmission)

    # price range
    if min_price.isdigit():
        cars = cars.filter(price__gte=int(min_price))

    if max_price.isdigit():
        cars = cars.filter(price__lte=int(max_price))

    # dropdown options for search page too
    models = Car.objects.values_list("model", flat=True).exclude(model__isnull=True).exclude(model__exact="").distinct().order_by("model")
    cities = Car.objects.values_list("city", flat=True).exclude(city__isnull=True).exclude(city__exact="").distinct().order_by("city")
    years = Car.objects.values_list("year", flat=True).exclude(year__isnull=True).distinct().order_by("year")
    body_styles = Car.objects.values_list("body_style", flat=True).exclude(body_style__isnull=True).exclude(body_style__exact="").distinct().order_by("body_style")
    transmissions = Car.objects.values_list("transmission", flat=True).exclude(transmission__isnull=True).exclude(transmission__exact="").distinct().order_by("transmission")

    return render(request, "cars/search.html", {
        "cars": cars,
        "query": q_text,
        "models": models,
        "cities": cities,
        "years": years,
        "body_styles": body_styles,
        "transmissions": transmissions,
        "selected": {
            "model": model,
            "city": city,
            "year": year,
            "body_style": body_style,
            "transmission": transmission,
            "min_price": min_price,
            "max_price": max_price,
        }
    })
