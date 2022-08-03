from django.contrib import admin
from .models import Customer, Cargo, Category, Invoice, Order, Truck, Driver, Location, WayBill
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'surname',
        'telephone_number',
        'passport',
        'email',
        'create_date',
        'update_date',
    )
    list_filter = ('is_delete', 'name', 'surname')
    search_fields = (
        'name',
        'surname',
        'telephone_number',
        'passport'
    )
    ordering = ('-create_date', )

class CargoAdmin(admin.ModelAdmin):
    list_display = (
        'length',
        'width',
        'higth',
        'volume',
        'weight',
        'category',
        'create_date',
        'update_date',
    )
    list_filter = ('volume', 'weight', 'category')
    search_fields = (
        'volume', 
        'weight', 
        'category'
    )
    ordering = ('-create_date', )
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'create_date',
        'update_date',
    )
    list_filter = ('name', )
    search_fields = ('name', )
    ordering = ('-create_date', )
    
class TruckAdmin(admin.ModelAdmin):
    list_display = (
        'truck_number',
        'weight',
        'volume',
        'brend',
        'model',
        'vin_code',
        'cargo_category',
        'create_date',
        'update_date',
    )
    search_fields = (
        'truck_number',
        'weight',
        'volume',
        'brend',
        'model',
        'vin_code',
        'cargo_category',
    )
    ordering = ('-create_date', )
    
class DriverAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'surname',
        'telephone_number',
        'passport',
        'driver_license',
        'cargo_category',
        'create_date',
        'update_date',
    )
    search_fields = (
        'name',
        'surname',
        'passport',
        'driver_license',
        'cargo_category',
    )
    list_filter = (
        'name',
        'surname',
        'passport',
        'driver_license',
        'cargo_category',
    )
        
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'country',
        'city',
        'address',
        'create_date',
        'update_date',
    )
    list_filter = filter = (
        'country',
        'city',
        'address'
    )
    search_fields = (
        'country',
        'city',
        'address'
    )
        
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'cargo',
        'point_a',
        'point_b',
        'create_date',
        'update_date',
    )   
    list_filter = filter = (
        'customer',
        'cargo',
        'point_a',
        'point_b',
    )
    search_fields = (
        'customer',
        'cargo',
        'point_a',
        'point_b',
    )
    
class WayBillAdmin(admin.ModelAdmin):
    list_display = (
        'drivers',
        'truck',
        'poin_a',
        'point_b',
        'create_date',
        'update_date',
    )
    list_filter = filter = (
        'drivers',
        'truck',
        'poin_a',
        'point_b',
    )
    search_fields = (
        'drivers',
        'truck',
        'poin_a',
        'point_b',
    )
    
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'invoice',
        'way_bill',
        'create_date',
        'update_date',
    )
    list_filter = filter = (
        'invoice',
        'way_bill',
        'create_date',
        'update_date',
    )
    search_fields = (
        'invoice',
        'way_bill',
        'create_date',
        'update_date',
    )
    
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Cargo, CargoAdmin) 
admin.site.register(Category, CategoryAdmin)
admin.site.register(Truck, TruckAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(WayBill, WayBillAdmin)
admin.site.register(Order, OrderAdmin)