from ..models import Car


class CarService:
    def __init__(self, car_id):
        self.ModelClass = Car
        self.__car = Car.objects.get(id=car_id)
        self.__id = car_id

    def get_car_object(self):
        return self.ModelClass.objects.select_for_update().get(id=self.__id)

    def update_mileage(self, mileage):
        self.__car.current_mileage = mileage
        self.__car.save()
        return self.__car.save()

    def get_car_type(self):
        return self.__car.type

    @staticmethod
    def get_car(**filter_args):
        return Car.objects.filter(**filter_args).first()