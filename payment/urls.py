from payment.apps import PaymentConfig
from rest_framework.routers import DefaultRouter
from payment.views import PaymentViewSet

app_name = PaymentConfig.name

router = DefaultRouter()
router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = [

              ] + router.urls
