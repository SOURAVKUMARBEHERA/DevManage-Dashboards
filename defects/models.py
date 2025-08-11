from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Developers(models.Model):
    dev_name = models.ForeignKey(User,on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    experience = models.IntegerField()
    def __str__(self):
        return self.dev_name.username
class Testers(models.Model):
    tester_name = models.ForeignKey(User,on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    experience = models.IntegerField()
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.tester_name.username
    
class defectsData(models.Model):

    defect_ID=models.CharField(max_length=100)
    defectName=models.CharField(max_length=100)
    assigned_by=models.ForeignKey(Testers,on_delete=models.CASCADE)
    assigned_to=models.ForeignKey(Developers,on_delete=models.CASCADE)
    description=models.TextField()
    defect_status=models.CharField(max_length=100)
    priority=models.CharField(max_length=100)
    assigned_date=models.DateField(auto_now_add=True)



    def __str__(self):
        return self.defectName
    
class defect_screenshot(models.Model):
    defect=models.ForeignKey(defectsData,on_delete=models.CASCADE)
    defect_img=models.ImageField(upload_to='defects_img/',blank=True,null=True)


