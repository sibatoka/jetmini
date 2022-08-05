from unicodedata import name
from django.db import models
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField

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
    telephone_number = PhoneNumberField(
        verbose_name='Номер телефона',
        unique=True,
        
    )
    passport = models.CharField(
        max_length=25,
        verbose_name='Номер пасспорта',
        unique=True
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания запсис'
    )
    is_delete = models.BooleanField(
        verbose_name='Удален',
        default=False
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления записи'
    )
    def __str__(self):
        return f'{self.surname} {self.name}'
    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        self.surname = self.surname.capitalize()
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('-create_date', )


class Cargo(models.Model):
    
    length = models.DecimalField(
        validators=[
            MinValueValidator(0)
        ],
        max_digits=12,
        decimal_places=2,
        verbose_name='Длина груза',
        help_text='м'
    )
    width = models.DecimalField(
        validators=[
            MinValueValidator(0)
        ],
        max_digits=12,
        decimal_places=2,
        verbose_name='Ширина груза',
        help_text='м'
    )
    higth = models.DecimalField(
        validators=[
            MinValueValidator(0)
        ],
        max_digits=12,
        decimal_places=2,
        verbose_name='Высота груза',
        help_text='м'
    )
    
    weight = models.DecimalField(
        validators=[
            MinValueValidator(0)
        ],
        max_digits=12,
        decimal_places=2,
        verbose_name='Вес',
        help_text='кг'
    )
    volume = models.DecimalField(
        validators=[
            MinValueValidator(0)
        ],
        max_digits=12,
        decimal_places=3,
        verbose_name='Объем',
        help_text='куб.м',
        blank=True,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        max_length=25,
        verbose_name='Категория груза'
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания запсис'
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления записи'
    )
    def __str__(self):
        return f'Груз №{self.id}'
    def save(self, *args, **kwargs):
        self.volume = self.higth * self.length * self.width
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'
        ordering = ('-create_date', )

        
class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название категории',    
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания запсис'
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления записи'
    )
    def __str__(self):
        return str(self.name)
       
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('-create_date', )

    
class Truck(models.Model):
        
    truck_number = models.CharField(
        max_length=25,
        verbose_name='Гос номер'
    )
    weight = models.DecimalField(
        validators=[
            MinValueValidator(0)
        ],
        max_digits=25,
        decimal_places=3,
        verbose_name='Грузоподъемность',
        help_text='тонн'
    )
    volume = models.DecimalField(
        validators=[
            MinValueValidator(0)
        ],
        max_digits=25,
        decimal_places=3,
        verbose_name='Объем',
        help_text='куб.м.',
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
        verbose_name='VIN код',
        unique=True
    )
    cargo_category = models.ManyToManyField(
        'Category',
        verbose_name='Категория груза',
        max_length=25,
        related_name="truck_categories"
        
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания запсис'
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления записи'
    )
    
    
    def get_categories(self):
        return '\n'.join(
            [category.name for category in self.cargo_category.all()]
        )
        
        
    def __str__(self):
        return f'{self.vin_code}|{self.truck_number}'
       
    class Meta:
        verbose_name = 'Грузовик',
        verbose_name_plural = 'Грузовики',
        ordering = ('-create_date', )

    
class Driver(models.Model):
        
    name = models.CharField(
        max_length=25,
        verbose_name='Имя'
    )
    surname = models.CharField(
        max_length=25,
        verbose_name='Фамилия'
    )
    telephone_number = PhoneNumberField(
        verbose_name='Номер телефона',
        unique=True,
        )
    passport = models.CharField(
        max_length=25,
        verbose_name='Номер пасспорта',
        unique=True
    )
    driver_license = models.CharField(
        max_length=25,
        verbose_name='Номер прав',
        unique=True
    )
    cargo_category = models.ManyToManyField(
        Category,
        verbose_name='Категория груза',
        max_length=25,
        related_name="driver_categories"
        
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания запсис'
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления записи'
    )
    
    
    def get_categories(self):
        return '\n'.join(
            [category.name for category in self.cargo_category.all()]
        )
        
        
    def __str__(self):
        return f'Водитель: {self.name} {self.surname}'
       
    class Meta:
        verbose_name = 'Водитель',
        verbose_name_plural = 'Водители',
        ordering = ('-create_date', )

    
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
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания запсис'
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления записи'
    )
    def __str__(self):
        return f'{self.country} {self.city}{self.address}'
       
    class Meta:
        verbose_name = 'Адрес',
        verbose_name_plural = 'Адреса',
        ordering = ('-create_date', )

        unique_together = ('country', 'city', 'address')
    
    
class Invoice(models.Model):
     
    customer = models.ForeignKey(
        Customer,
         on_delete=models.PROTECT
    )   
    cargo = models.ManyToManyField(
        Cargo,
        related_name='my_cargos',
        verbose_name='Мои грузы',
    )
    point_a = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        related_name='invoice_loaction_a'
    )
    point_b = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        related_name='invoice_loaction_b',
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания запсис'
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления записи'
    )

    
    def get_cargos(self):
        return '\n'.join(
            [str(cargo) for cargo in self.cargo.all()]
        )
        
        
    def __str__(self):
        return f'Заявка № {self.id}'
       
    class Meta:
        verbose_name = 'Заявка',
        verbose_name_plural = 'Заявки',
        ordering = ('-create_date', )

    
class WayBill(models.Model):
    
    drivers = models.ForeignKey(
        'Driver',
        on_delete=models.PROTECT
    )
    truck = models.ForeignKey(
        'Truck',
        on_delete=models.PROTECT,
    )
    point_a = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        related_name='waybill_loaction_a'
    )
    point_b = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        related_name='waybill_loaction_b'
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания запсис'
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления записи'
    )
    def __str__(self):
        return f'Путивой лист № {self.id}'
       
    class Meta:
        verbose_name = 'Путивой лист',
        verbose_name_plural = 'Путевые листы',
        ordering = ('-create_date', )

    
class Order(models.Model):
    
    invoice = models.ManyToManyField(
        Invoice,
    )
    way_bill = models.OneToOneField(
        WayBill,
        on_delete=models.CASCADE,
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания запсис'
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления записи'
    )
    
    def get_invoices(self):
        return '\n'.join(
            [str(invoice) for invoice in self.invoice.all()]
        )
    
        
    def __str__(self):
        return f'Заказ № {self.id}'
       
    class Meta:
        verbose_name = 'Заказ',
        verbose_name_plural = 'Заказы',
        ordering = ('-create_date', )
