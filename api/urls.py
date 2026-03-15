from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import *
urlpatterns = [
    path('google_login/',GoogleLoginView.as_view(),name="google_view"),
    path('register/',RegisterView.as_view(),name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('blog/', BlogView.as_view(), name='blog_view'),
    path('blog/<int:pk>/', BlogRetreiveView.as_view(), name='blog_retrieve_view'),
    
    path('tech/', TechnologyView.as_view(), name='tech_view'),
    path('tech/<int:pk>/', TechnologyRetreiveView.as_view(), name='tech_retrieve_view'),
    
    path('design/', DesignView.as_view(), name='design_view'),
    path('design/<int:pk>/', DesignRetreiveView.as_view(), name='design_retrieve_view'),
    
    path('programming/', ProgrammingView.as_view(), name='programming_view'),
    path('programming/<int:pk>/',   ProgrammingRetreiveView.as_view(), name='programming_retrieve_view'),
    
    path('lifestyle/', LifesyleView.as_view(), name='lifestyle_view'),
    path('lifestyle/<int:pk>/', LifesyleRetreiveView.as_view(), name='lifestyle_retrieve_view'),
    
    path('contact/', ContactView.as_view(), name='contact_view'),
    path('contact/<int:pk>/', ContactRetreiveView.as_view(), name='contact_retrieve_view'),
]