from rest_framework import viewsets

from .serializers import (TruckSerializer, InvoiceSerializer, OrderSerializer, DriverSerializer, 
                     CustomerSerializer, CategorySerializer, CargoSerializer, LocationSerializer,
                     WaybillSerializer)

from .models import (Truck, Invoice, Order, Driver, 
                     Customer, Category, Cargo, Location, WayBill)

# Create your views here.

class TruckApiView(viewsets.ModelViewSet):
    
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()
    
    
class CargoApiView(viewsets.ModelViewSet):
    
    serializer_class = CargoSerializer
    queryset = Cargo.objects.all()
  
    
class InvoiceApiView(viewsets.ModelViewSet):
    
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
   
    
class OrderApiView(viewsets.ModelViewSet):
    
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    
    
class DriverApiView(viewsets.ModelViewSet):
    
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()


class CustomerApiView(viewsets.ModelViewSet):
    
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    
    
class CategoryApiView(viewsets.ModelViewSet):
    
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    

class LocationApiView(viewsets.ModelViewSet):
    
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    
    
class WaybillApiView(viewsets.ModelViewSet):
    
    serializer_class = WaybillSerializer
    queryset = WayBill.objects.all()