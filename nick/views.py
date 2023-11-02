
from rest_framework import viewsets
from nick.models import Company,Employee
from nick.serializers import CompanySerializers,EmployeeSerializers
from rest_framework.decorators import action

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers

    @action(detail=True,methods=['get','post'])
    def employee(self,request,pk=None):
        pass

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers