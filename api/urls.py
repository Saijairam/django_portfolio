from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
router  = DefaultRouter()

router.register('project',views.Portfolioview,basename='project')
router.register('experience',views.Expview,basename='experience')

urlpatterns = [ 
    path('',include(router.urls))
]


