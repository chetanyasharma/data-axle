from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from dataaxle.drf_utils import Response
from dataaxle.exception_handler import exception_handler
from .serializers import RentaRregistrationCreateSerializer, \
    RentaRregistrationUpdateSerializer
from .services.rent_registration import RentaRegistrationService


class RentRegistrationView(APIView):
    permission_classes = [AllowAny]
    create_serializer_class = RentaRregistrationCreateSerializer
    update_serializer_class = RentaRregistrationUpdateSerializer
    rentservice = RentaRegistrationService()

    @exception_handler(api_level=True)
    def post(self, request):
        serializer = self.create_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        car_id = serializer.validated_data['car_id']
        serializer.validated_data.pop('car_id')
        reg_obj = self.rentservice.rent_car(car_id, **serializer.validated_data)
        return Response({"customer_name": "{f_name} {l_name}".format(f_name=reg_obj.customer_first_name,
                                                                     l_name=reg_obj.customer_last_name),
                         "customer_booking_number": reg_obj.id})

    @exception_handler(api_level=True)
    def put(self, request):
        serializer = self.update_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer_booking_number = serializer.validated_data['customer_booking_number']
        serializer.validated_data.pop('customer_booking_number')
        price = self.rentservice.retrun_car(customer_booking_number, **serializer.validated_data)
        return Response({"rental_price": price}, code=201)
