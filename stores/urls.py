from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stores/', views.StoreLocation.as_view()),
    path('nearest_locations/<str:postcode>/<int:distance>',views.NearestStoresToLocation.as_view(),name='nearest_lcoations')
    ]
urlpatterns = format_suffix_patterns(urlpatterns)