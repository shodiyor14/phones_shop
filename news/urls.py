from django.urls import path
from news.views import NewsListView, NewsDetailView

app_name = 'news'

urlpatterns = [
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('', NewsListView.as_view(), name='news')
]