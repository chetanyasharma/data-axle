from sqlite3 import OperationalError

from django.db import models,transaction

from dataaxle.models import BaseModel


class CarType(models.TextChoices):
    COMPACT = 'compact'
    PREMIUM = 'premium'
    MINIVAN = 'minivan'

class Car(BaseModel):
    name = models.CharField(max_length=254, null=True, blank=True)
    vehicle_number = models.CharField(max_length=16, null=True, blank=True, db_index=True, unique=True)
    type = models.CharField(choices=CarType.choices, max_length=128, null=True, blank=True)
    booked_status = models.BooleanField(default=False)
    current_rent_registration = models.OneToOneField('RentaRregistration', on_delete=models.PROTECT, null=True, blank=True)


    class Meta:
        db_table = 'cars'


class RentaRregistration(BaseModel):
    customer_first_name = models.CharField(max_length=254, null=True)
    customer_last_name = models.CharField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=16, null=True, blank=True)
    pickup_pre_book_date = models.DateField(null=True, blank=True, editable=False)
    current_mileage_pickup = models.FloatField(null=True, blank=True, default=0)
    current_mileage_return = models.FloatField(null=True, blank=True, default=0)
    datetime_of_pickup = models.DateTimeField(null=True, blank=True, editable=False)
    datetime_of_return = models.DateTimeField(null=True, blank=True, editable=False)
    kilometer_run = models.FloatField(null=True, blank=True, default=0)
    rental_price = models.FloatField(null=True, blank=True, default=0)

    class Meta:
        db_table = 'renta_registration'
