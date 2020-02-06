from django.db import models
from application.models.vendor import vendor
from application.models.user import user

class bill(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True)
    vendor=models.ForeignKey(vendor,on_delete=models.CASCADE)
    bill_date=models.DateField()
    items = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    tax = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    class Meta:
        db_table="bill"
