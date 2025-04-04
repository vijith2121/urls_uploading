from django.urls import path, include
from .views import index, get_url, admin_items, download_csv, delete_all_urls

urlpatterns = [
    path('', index, name='index'),
    path('get_url', get_url, name='get_url'),
    path('admin_fynkom', admin_items, name='admin_items'),
    path('download-csv/', download_csv, name='download_csv'),
    path('delete-data/', delete_all_urls, name='delete_all_urls'),
]
