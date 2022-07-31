from string import digits
from django.db import models
from pytz import country_names

# Create your models here.
class Customer(models.Model):
    name = models.CharField(
        max_length=70,
        verbose_name='Имя',
    )
    surname = models.CharField(
        max_length=70,
        verbose_name='Фамилия',
    )
    telephone_number = models.IntegerField(
        max_length=15,
        verbose_name='Номер телефона',
        digits=True,
    )
    passport = models.CharField(
        max_length=25,
        verbose_name='Номер пасспорта',
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
    )

class Cargo(models.Model):
    
    weight = models.DecimalField(
        max_digits=7,
        verbose_name='Вес в кг.',
    )
    volume = models.DecimalField(
        max_digits=7,
        verbose_name='Объем в куб.м',
    )
    category = models.CharField(
        max_length=25,
        verbose_name='Категория груза'
    )
    
class Truck(models.Model):
    
    truck_number = models.CharField(
        max_length=25,
        verbose_name='Гос номер'
    )
    weight = models.DecimalField(
        max_digits=25,
        verbose_name='Грузоподъемность'
    )
    volume = models.DecimalField(
        max_digits=25,
        verbose_name='Объем'
    )
    brend = models.CharField(
        max_length=25,
        verbose_name='Марка'
    )
    model = models.CharField(
        max_length=25,
        verbose_name='Модель'
    )
    vin_code = models.CharField(
        max_length=25,
        verbose_name='VIN код'
    )
    cargo_categoty = models.CharField(
        max_length=25,
        verbose_name='Категория груза'
    )
    
    
class Driver(models.Model):
        
    name = models.CharField(
        max_length=25,
        verbose_name='Имя'
    )
    surname = models.CharField(
        max_length=25,
        verbose_name='Фамилия'
    )
    telephone_number = models.IntegerField(
        max_length=25,
        verbose_name='Номер телефона'
    )
    passport = models.CharField(
        max_length=25,
        verbose_name='Номер пасспорта',
    )
    driver_license = models.CharField(
        max_length=25,
        verbose_name='Номер прав'
    )
    cargo_category = models.CharField(
        max_length=25,
        verbose_name='Категория груза'
    )
    
class Location(models.Model):
    
    city = models.CharField(
        max_length=25,
        verbose_name='Город'
    )
    country = models.CharField(
        max_length=25,
        verbose_name='Страна'
    )
    address = models.CharField(
        max_length=25,
        verbose_name='Адрес'
    )
    
class Invoice(models.Model):
     
    customer = models.ForeignKey(
         'Invoice',
         on_delete=models.CASCADE
    )   
    cargo = models.ForeignKey(
        'Cargo',
        on_delete=models.CASCADE
    )
    point_a = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE
    )
    point_b = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
    )
    
class WayBill(models.Model):
    
    drivers = models.ForeignKey(
        'Driver',
        on_delete=models.CASCADE
    )
    truck = models.ForeignKey(
        'Truck',
        on_delete=models.CASCADE,
    )
    point_a = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE
    )
    point_b = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
    )
    
class Order(models.Model):
    
    invoice = models.ForeignKey(
        'Invoice',
        on_delete=models.CASCADE
    )
    way_bill = models.ForeignKey(
        'WayBill',
        on_delete=models.CASCADE,
    )