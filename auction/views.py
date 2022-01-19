from rest_framework.viewsets import ModelViewSet
from .models import Auction
from .serializers import AuctionSerializer

# Create your views here.
class AuctionViewset(ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer