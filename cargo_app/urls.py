from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import(CargoApiView, TruckApiView, OrderApiView, InvoiceApiView, DriverApiView, 
                     CustomerApiView, CategoryApiView, LocationApiView, WaybillApiView) 


router = SimpleRouter()

router.register('cargo', CargoApiView, basename='cargo')
router.register('truck', TruckApiView, basename='truck')
router.register('order', OrderApiView, basename='order')
router.register('invoice', InvoiceApiView, basename='invoice')
router.register('driver', DriverApiView, basename='driver')
router.register('customer', CustomerApiView, basename='customer')
router.register('category', CategoryApiView, basename='category')
router.register('location', LocationApiView, basename='location')
router.register('waybill', WaybillApiView, basename='waybill')



urlpatterns =[
    
] + router.urls