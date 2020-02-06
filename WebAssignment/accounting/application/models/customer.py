from django.db import models
from application.models.user import user

class customer(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    class Meta:
        db_table="customer"
