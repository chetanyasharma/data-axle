from django.db import transaction

from .car import CarService
from ..models import RentaRregistration, CarType


class RentaRegistrationService:
    base_day_rental = 10
    kilometer_price = 20

    def __init__(self):
        self.ModelClass = RentaRregistration
        self.__car_service = CarService

    @transaction.atomic
    def rent_car(self, car_id, **kwargs):
        registration = self.ModelClass.objects.create(**kwargs)
        car_obj = self.__car_service(car_id).get_car_object()
        if car_obj.booked_status:
            raise AttributeError('car already booked')
        car_obj.current_rent_registration = registration
        car_obj.booked_status = True
        car_obj.save()
        return registration

    @transaction.atomic
    def retrun_car(self, booking_id, **kwargs):
        customer_booking_number = booking_id
        rent_obj = self.ModelClass.objects.get(id=customer_booking_number)
        days_used = (rent_obj.datetime_of_pickup.date()-kwargs['datetime_of_return'].date())
        car = self.get_car(customer_booking_number)
        car.booked_status=False
        car.save()
        rental_price = self.rental_period_price(days_used.days,car.type,kwargs['kilometer_run'])
        kwargs.update(rental_price=rental_price)
        registration = self.ModelClass.objects.filter(id=booking_id).update(**kwargs)
        return rental_price

    def rental_period_price(self, days_used, car_type, total_travel):
        if car_type == CarType.COMPACT:
            price = self.base_day_rental * days_used
        elif car_type == CarType.PREMIUM:
            price = (self.base_day_rental * days_used * 1.2) + (self.kilometer_price * total_travel)
        elif car_type == CarType.MINIVAN:
            price = (self.base_day_rental * days_used * 1.7) + (self.kilometer_price * total_travel * 1.5)
        else:
            raise AttributeError("invalid type")
        return price

    def get_car(self,customer_booking_number):
        return self.__car_service.get_car(current_rent_registration=customer_booking_number)
