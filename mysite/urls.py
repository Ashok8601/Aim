from django.urls import path
from polls import views  # अगर views इसी app में हैं

urlpatterns = [
    path('', views.home, name='home'),  # 👈 ये root URL है (homepage)
]
