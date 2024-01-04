from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class CarPool(models.Model):
    name = models.CharField(blank=True)
    carModel = models.CharField(max_length=200)
    departureTime = models.IntegerField(default=0)
    arrivalTime = models.IntegerField(default=0)
    route = models.CharField(max_length=200)
    availableSeats = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('carpool:myCarpool')
# class CarPool:
#     def __init__(self, carpoolid, carModel, route, availableSeats):
#         self.carpoolid = carpoolid
#         self.carModel = carModel
#         self.route = route
#         self.availableSeats = availableSeats
#
#
# carPool1 = CarPool(carpoolid="1001",carModel="Honda Accord", route="Arlington - Falls Church", availableSeats="2")
# carPool2 = CarPool(carpoolid="1002",carModel="Toyota Camry", route="West Falls Church - Tyson", availableSeats="3")
# carPool3 = CarPool(carpoolid="1003",carModel="Ford Focus", route="Silver Spring - Rockville", availableSeats="1")
# carPool4 = CarPool(carpoolid="1004",carModel="Honda Civic", route="Alexandria - Arlington", availableSeats="1")
# carPool5 = CarPool(carpoolid="1005",carModel="Toyota Corolla", route="Ashburn - Tyson", availableSeats="2")
# carPool6 = CarPool(carpoolid="1006",carModel="Ford Explorer", route="Silver Spring - Rockville", availableSeats="3")
# carPool7 = CarPool(carpoolid="1007",carModel="Honda Odyssey", route="Arlington - Falls Church", availableSeats="3")
# carPool8 = CarPool(carpoolid="1008",carModel="Toyota Tacoma", route="Washington - Bethesda", availableSeats="1")
# carPool9 = CarPool(carpoolid="1009",carModel="Ford Edge", route="Tyson Corner - Alexandria", availableSeats="2")
#
#
# carpools = [carPool1, carPool2, carPool9, carPool8,
#             carPool7, carPool6, carPool5, carPool4, carPool3]

# carpools = []

regular_user = {"username": "rick", "password": "regular"}
