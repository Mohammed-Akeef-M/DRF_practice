
from django.contrib import admin
from django.urls import path
from app.views import employeeListView, userlist, employeeDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employee', employeeListView ),
    path('api/users', userlist),
    path('api/employee/<int:pk>', employeeDetailView)

]
