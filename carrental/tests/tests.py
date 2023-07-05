import pytest
from rest_framework import status

from dataaxle.exception_handler import ExceptionCreator
from ..models import CarType, Car, RentaRregistration
from ..services.rent_registration import RentaRegistrationService
from django.test.client import RequestFactory
from unittest import mock
from rest_framework.exceptions import APIException
from rest_framework.test import APIClient
from.fixtures import dummy__rental_registar_data,dummy__negative_rental_registar_data,dummy__negative_retun_car_data,dummy__return_car_data
from unittest.mock import Mock



class TestRentaRegistrationServiceUnittest:
    @pytest.mark.parametrize('car_type', list(CarType.values))
    def test_rental_period_price_postive(self, car_type, days_used=50, total_travel=21.5):
        """
        Testing for Postive flow of function 'rental_period_price'
        """
        base_day_rental = 10
        kilometer_price = 20
        rent_cls_ = RentaRegistrationService()
        desired_price = None
        if car_type == CarType.COMPACT:
            desired_price = base_day_rental * days_used
        elif car_type == CarType.PREMIUM:
            desired_price = (base_day_rental * days_used * 1.2) + (kilometer_price * total_travel)
        elif car_type == CarType.MINIVAN:
            desired_price = (base_day_rental * days_used * 1.7) + (kilometer_price * total_travel * 1.5)
        else:
            pass
        price = rent_cls_.rental_period_price(days_used, car_type, total_travel)
        assert price == desired_price

    def test_rental_period_price_negative(self, days_used=50, car_type='random', total_travel=21.5):
        """
        Testing for negative flow of function 'rental_period_price'
        """
        with pytest.raises(AttributeError) as exc_info:
            price = RentaRegistrationService().rental_period_price(days_used, car_type, total_travel)
        assert exc_info.type is AttributeError



@pytest.mark.integtest
class TestRentalRegistar:
    def __submit_api_request(self, data: dict):
        response = APIClient().post(f'/car_rental/rental_registar', data=data, format='json')
        return response

    @pytest.mark.usefixtures('dummy__negative_rental_registar_data')
    def test_negative_api(self):
        """
        Testing for negative flow of api
        """
        mockObject = RentaRegistrationService
        mockObject.rent_car = Mock(return_value=self.output_data)
        response_data = self.__submit_api_request(self.input_data)
        assert response_data.status_code == status.HTTP_400_BAD_REQUEST

    @pytest.mark.parametrize('car_type', list(CarType.values))
    @pytest.mark.usefixtures('dummy__rental_registar_data')
    def test_postive_api(self,car_type):
        """
            Testing for postive flow of api
        """
        mock_rental = mock.MagicMock(spec=RentaRregistration)
        mock_rental.id = 'd2018f83-ca83-448c-b151-9d87992c77'
        mock_rental.customer_first_name = 'newbie'
        mock_rental.customer_last_name = 'sharma'
        mock_rental.phone_number = "010201"
        mock_rental.current_mileage_pickup = 12.23
        mock_rental.pickup_pre_book_date = "2022-02-13"
        mock_rental.datetime_of_pickup = "2022-02-13"
        ren_mock_obj = RentaRegistrationService
        ren_mock_obj.rent_car = Mock(return_value=mock_rental)
        response_data = self.__submit_api_request(self.input_data)
        assert response_data.status_code == status.HTTP_200_OK
#
@pytest.mark.integtest
class TestReturnCar:
    def __submit_api_request(self, data: dict):
        response = APIClient().put(f'/car_rental/return_car', data=data, format='json')
        return response

    @pytest.mark.usefixtures('dummy__negative_retun_car_data')
    def test_negative_api(self):
        """
            Testing for negative flow of api
        """
        ren_mock_obj = RentaRegistrationService
        ren_mock_obj.rent_car = Mock(return_value=self.output_data)
        response_data = self.__submit_api_request(self.input_data)
        assert response_data.status_code == status.HTTP_400_BAD_REQUEST

    @pytest.mark.parametrize('car_type', list(CarType.values))
    @pytest.mark.usefixtures('dummy__return_car_data')
    def test_postive_api(self, car_type):
        """
            Testing for postive flow of api
        """
        ren_mock_obj = RentaRegistrationService
        ren_mock_obj.retrun_car = Mock(return_value=1420)
        response_data = self.__submit_api_request(self.input_data)
        assert response_data.status_code == status.HTTP_200_OK