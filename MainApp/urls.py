from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payments/', include('Payments.urls')),
    path("", views.rag_agent, name="index"),
    
]
