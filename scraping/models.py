from django.db import models
# Create your models here.
class Main(models.Model):
    ticker = models.CharField(max_length=10)
    open_price = models.DecimalField(max_digits=20, decimal_places=15)
    low_price = models.DecimalField(max_digits=20, decimal_places=15)
    profit = models.DecimalField(max_digits=20, decimal_places=15)
    risk = models.DecimalField(max_digits=20, decimal_places=15)
    new_candidate = models.CharField(max_length=10)
