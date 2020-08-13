from django.urls import path
from app7 import views
app_name="app7"


urlpatterns = [
    path('img/',views.img_upld,name="img"),
]
