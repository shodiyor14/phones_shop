from django.urls import path
from phones.views import HomeTemplateView, PhonesListView

app_name = 'phones'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('phones/', PhonesListView.as_view(),name='products')
]