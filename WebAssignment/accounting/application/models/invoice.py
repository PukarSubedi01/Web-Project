from django.db import models
from application.models.customer import customer
from application.models.user import user

class invoice(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True)
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    invoice_date=models.DateField()
    items = models.CharField(max_length=100);
    quantity = models.CharField(max_length=100);
    price = models.CharField(max_length=100);
    tax = models.CharField(max_length=100);
    total = models.CharField(max_length=100);
    user = models.ForeignKey(user, on_delete=models.CASCADE)

    class Meta:
        db_table="invoice"
