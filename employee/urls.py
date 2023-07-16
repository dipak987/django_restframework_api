from django.urls import path
from .views import EmployeeListCreate, EmployeeRetrieveUpdateDelete


urlpatterns = [
    path('employee', EmployeeListCreate.as_view(), name="Create-Employee-List"),
    path('employee/<int:pk>/',EmployeeRetrieveUpdateDelete.as_view(), name='employee-Details')
]