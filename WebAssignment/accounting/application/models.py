from django.db import models
class user(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True)
    fullname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    class Meta:
        db_table="user"


