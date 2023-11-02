from rest_framework import routers
from nick.views import CompanyViewSet,EmployeeViewSet
from django.urls import path,include

router = routers.DefaultRouter()
router.register('companies',CompanyViewSet)
router.register('employees',EmployeeViewSet)


urlpatterns = [
    path('',include(router.urls))
]