from django.urls import path
from . import views

# api/info
# api/info/month
# api/info/year
urlpatterns = [
    path("info/", views.api_info, name="general-info"),
    path("info/month/", views.month_info, name="month-info"),
    path("info/year/", views.year_info, name="year-info")
]
