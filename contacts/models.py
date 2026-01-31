from django.db import models
from django.utils import timezone

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    car_id = models.IntegerField()  # or ForeignKey later
    customer_need = models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)

    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)

    message = models.TextField(blank=True)

    user_id = models.IntegerField(null=True, blank=True)

    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
