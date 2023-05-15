from django.db import models

# Create your models here.

#booking model
class Booking(models.Model):
    name = models.CharField(max_length=200)
    number_of_seats = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return self.name


#menu model
class Menu(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

    def __str__(self):
        return f'{self.title} : {str(self.price)}'