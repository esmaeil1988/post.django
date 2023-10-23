from django.db import models

# Create your models her
class doctor(models.Model):
    nam=models.CharField(max_length=20)
    famil=models.CharField(max_length=20)
    takhasos=models.CharField(max_length=80)
    adress=models.CharField(max_length=40)
    tozih=models.CharField(max_length=890,null=True)
    img=models.ImageField(upload_to='aks',null=True)
    def __str__(self) -> str:
        return self.nam+' '+self.famil
    
class contact(models.Model):
    nam=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    onvan=models.CharField(max_length=30)
    matn=models.CharField(max_length=500)
    img=models.ImageField(upload_to='aks',null=True)
    def __str__(self) -> str:
        return self.onvan
    
class news(models.Model):
    onvan=models.CharField(max_length=50)
    matn=models.CharField(max_length=800)
    manba=models.CharField(max_length=40)
    aks=models.ImageField(upload_to='aks', null=True)
    def __str__(self) -> str:
        return self.onvan