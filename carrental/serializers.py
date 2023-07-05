from django.utils import timezone
from rest_framework import serializers


class RentaRregistrationCreateSerializer(serializers.Serializer):
    customer_first_name = serializers.CharField(max_length=254, required=True)
    customer_last_name = serializers.CharField(max_length=254, required=True)
    phone_number = serializers.CharField(max_length=16, required=True)
    current_mileage_pickup = serializers.FloatField(required=True)
    car_id = serializers.CharField(required=True)
    pickup_pre_book_date = serializers.DateField(required=True)
    datetime_of_pickup = serializers.DateTimeField(required=True)
    picked_up = serializers.BooleanField(required=True, allow_null=False)

    def validate(self, data):
        picked_up = data.get('picked_up', False)
        data.pop('picked_up')
        if not picked_up and not data.get('pickup_pre_book_date', None):
            raise "pickup_pre_book_date needed"
        if picked_up:
            data['datetime_of_pickup'] = timezone.now()
        return data


class RentaRregistrationUpdateSerializer(serializers.Serializer):
    customer_booking_number = serializers.CharField(max_length=254, required=True)
    current_mileage_return = serializers.FloatField(required=True)
    datetime_of_return = serializers.DateTimeField(required=True)
    kilometer_run = serializers.FloatField(required=True)

    def validate(self, data):
        datetime_of_return = data.get('datetime_of_return', False)
        if not datetime_of_return:
            data['datetime_of_return'] = timezone.now()
        return data
