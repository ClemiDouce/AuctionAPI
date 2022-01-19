from rest_framework.routers import DefaultRouter

from comment.views import CommentViewset

router = DefaultRouter()
router.register('', CommentViewset, basename="comments")


urlpatterns = router.urls