from django.urls import path
from .views import HomePageView, PostPageView, AboutPageView, PostDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', PostPageView.as_view(), name='post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('about/', AboutPageView.as_view(), name='about')
]
