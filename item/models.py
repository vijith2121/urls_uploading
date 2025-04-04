from django.db import models
from datetime import date
from django.utils.timezone import now
# Create your models here.

class GetUrls(models.Model):
    url = models.TextField()
    # scrape_date = date.today()
    scrape_date = models.DateTimeField(default=now)