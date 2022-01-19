from rest_framework.routers import DefaultRouter
from .views import AuctionViewset

router = DefaultRouter()
router.register('', AuctionViewset, basename="auctions")

urlpatterns = router.urls