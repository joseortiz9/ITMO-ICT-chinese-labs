from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'conference',Conference_viewsets,basename = 'conference')
router.register(r'review',Review_viewsets,basename = 'review')
router.register(r'user',User_viewsets,basename = 'user')
router.register(r'presentation',Presentation_viewsets,basename = 'presentation')

urlpatterns = router.urls