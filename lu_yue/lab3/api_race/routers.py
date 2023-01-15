from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'race',Race_viewsets,basename = 'race')
router.register(r'team',Team_viewsets,basename = 'team')
router.register(r'rider',Rider_viewsets,basename = 'rider')
router.register(r'comment',Comment_viewsets,basename = 'comment')
urlpatterns = router.urls