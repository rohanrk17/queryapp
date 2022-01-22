from django.urls import path
from .views import UserRolesView

urlpatterns = [
    path('roleusers/<str:role>', UserRolesView.as_view(), name='token_obtain_pair'),
    
]