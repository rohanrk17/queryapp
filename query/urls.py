from django.urls import path
from .views import QueryView,UserPostsView

urlpatterns = [
    path('postquery/', QueryView.as_view(), name='postquery'),
    path('userqueries/<str:email>', UserPostsView.as_view(), name='userqueries'),
]