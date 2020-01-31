from django.db import models
from application.models.vendor import vendor

class bill(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True)
    vendor=models.ForeignKey(vendor,on_delete=models.CASCADE)
    bill_date=models.DateField()
    items = models.CharField(max_length=100);
    quantity = models.CharField(max_length=100);
    price = models.CharField(max_length=100);
    tax = models.CharField(max_length=100);
    total = models.CharField(max_length=100);

    class Meta:
        db_table="bill"
