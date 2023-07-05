import pytest


@pytest.fixture(scope='class')
def dummy__rental_registar_data(request):
    input_dict = {"customer_first_name": "newbie",
                  "customer_last_name": "sharma",
                  "phone_number": "010201",
                  "current_mileage_pickup": 12.23,
                  "car_id": "d2018f83-ca83-448c-b151-9d87992c77",
                  "pickup_pre_book_date": "2022-02-13",
                  "picked_up": True,
                  "datetime_of_pickup": "2022-02-13"}
    output_dict = {
        "data": {
            "customer_name": "newbie sharma",
            "customer_booking_number": "4db20dc6-640a-4486-8d47-926883ad0d09"
        },
        "msg": "",
        "code": 200
    }
    request.cls.input_data = input_dict
    request.cls.output_data = output_dict

@pytest.fixture(scope='class')
def dummy__negative_rental_registar_data(request):
    input_dict = {"customer_first_name": "newbie",
                  "customer_last_name": "sharma",
                  "current_mileage_pickup": 12.23,
                  "car_id": "d2018f83-ca83-448c-b151-9d87992c77",
                  "pickup_pre_book_date": "2022-02-13",
                  "picked_up": True,
                  "datetime_of_pickup": "2022-02-13"}
    output_dict = {
        "data": {
            "customer_name": "newbie sharma",
            "customer_booking_number": "4db20dc6-640a-4486-8d47-926883ad0d09"
        },
        "msg": "",
        "code": 200
    }
    request.cls.input_data = input_dict
    request.cls.output_data = output_dict

@pytest.fixture(scope='class')
def dummy__negative_retun_car_data(request):
    input_dict = {
    "customer_booking_number":"d390a112-cc80-48b2-b1f3-49be7e847f55",
    "kilometer_run":12.4
}
    output_dict = {
        "data": {
            "rental_price": 0
        },
        "msg": "",
        "code": 201
    }
    request.cls.input_data = input_dict
    request.cls.output_data = output_dict

@pytest.fixture(scope='class')
def dummy__return_car_data(request):
    input_dict = {
    "customer_booking_number":"611349ff-13d0-429b-851a-14b17dc95a09",
    "current_mileage_return":12.2,
    "kilometer_run":12.4,
    "datetime_of_return":"2023-02-13"
    }
    output_dict = {
        "data": {
            "rental_price": 1420
        },
        "msg": "",
        "code": 201
    }
    request.cls.input_data = input_dict
    request.cls.output_data = output_dict