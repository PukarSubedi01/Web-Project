from django.db import models


class customer(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    class Meta:
        db_table="customer"
