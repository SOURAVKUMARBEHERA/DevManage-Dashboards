from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userData(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)



    # additional field
    Door_no=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.IntegerField()
    profile_pic=models.ImageField(upload_to='userimg',null=True,blank=True)


