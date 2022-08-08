from rest_framework import serializers

from .models import (Truck, Invoice, Order, Driver, 
                     Customer, Category, Cargo, Location, WayBill)


class TruckSerializer(serializers.ModelSerializer):
    
    cargo_category = serializers.StringRelatedField(
        read_only=True
    )
    
    class Meta: 
        model = Truck
        fields = '__all__'
  
        
class CargoSerializer(serializers.ModelSerializer):
    
    category = serializers.StringRelatedField(
        read_only=True
    )
    
    class Meta: 
        model = Cargo
        fields = '__all__'
        
                      
class InvoiceSerializer(serializers.ModelSerializer):

    customer = serializers.StringRelatedField(
        read_only=True
    )
    cargo = CargoSerializer(many=True, read_only=True)
     
    point_a = serializers.StringRelatedField(
        read_only=True
    )
    
    point_b = serializers.StringRelatedField(
        read_only=True
    )
    class Meta: 
        model = Invoice
        fields = '__all__'
        

class DriverSerializer(serializers.ModelSerializer):
    
    cargo_category = serializers.StringRelatedField(
        read_only=True
    )
    
    class Meta: 
        model = Driver
        fields = '__all__'


class WaybillSerializer(serializers.ModelSerializer):
    
    drivers = DriverSerializer(read_only=True)
    
    truck = TruckSerializer(read_only=True)
    
    point_a = serializers.StringRelatedField(
        read_only=True
    )
    
    point_b = serializers.StringRelatedField(
        read_only=True
    )
    
    class Meta: 
        model = WayBill
        fields = '__all__'
    
        
class OrderSerializer(serializers.ModelSerializer):
    
    invoice = InvoiceSerializer(many=True, read_only=True)
    way_bill = WaybillSerializer()
    
    class Meta: 
        model = Order
        fields = '__all__'
        
              
class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Customer
        fields = '__all__'
             
             
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Category
        fields = '__all__'
    
      
class LocationSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Location
        fields = '__all__'
        