from django.shortcuts import render, redirect
from .models import GetUrls
# Create your views here.
import csv
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def get_url(request):
    if request.method == 'POST':
        urls = request.POST.get('urls')
        if urls:
            GetUrls.objects.create(url=urls)
    return redirect('index')


def admin_items(request):
    items_data = GetUrls.objects.all()
    return render(request, 'admin_templates.html', {'items_data': items_data})


def download_csv(request):
    # Create the HTTP response with CSV content type
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="urls_data.csv"'

    # Create CSV writer
    writer = csv.writer(response)
    
    # Write CSV header
    writer.writerow(['ID', 'URL', 'Scrape Date'])
    
    # Fetch data from database and write rows
    for item in GetUrls.objects.all():
        writer.writerow([item.id, item.url, item.scrape_date])

    return response

def delete_all_urls(request):
    GetUrls.objects.all().delete()  # Deletes all records
    return redirect('/?deleted=true')