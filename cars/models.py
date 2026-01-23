from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


class Car(models.Model):

    STATE_CHOICES = (
        ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'),
        ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'),
        ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'),
        ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'),
        ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'),
        ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'),
        ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'),
        ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'),
        ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'),
        ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'),
        ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'),
    )

    YEAR_CHOICES = [(r, r) for r in range(2000, datetime.now().year + 1)]

    FEATURES_CHOICES = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    DOOR_CHOICES = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=STATE_CHOICES, max_length=2)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(choices=YEAR_CHOICES)
    body_style = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)  # "New/Used"
    description = RichTextField()

    price = models.IntegerField()

    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', max_length=255)
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', max_length=255, blank=True, null=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', max_length=255, blank=True, null=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', max_length=255, blank=True, null=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', max_length=255, blank=True, null=True)

    features = MultiSelectField(choices=FEATURES_CHOICES, max_length=300, blank=True)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100)

    miles = models.IntegerField()
    doors = models.CharField(choices=DOOR_CHOICES, max_length=1)
    passengers = models.IntegerField()

    vin_no = models.CharField(max_length=100)
    no_of_owners = models.CharField(max_length=100, blank=True)

    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title
