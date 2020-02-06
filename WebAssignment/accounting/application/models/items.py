from django.db import models
from application.models.user import user

class items(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True)
    item_name=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    purchase_price=models.CharField(max_length=100)
    sales_price=models.CharField(max_length=100)
    tax=models.CharField(max_length=100)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    class Meta:
        db_table="items"
