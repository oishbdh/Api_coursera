from django.db import models

# Create your models here.

class Category(models.Model):
     slug = models.SlugField()
     title = models.CharField(max_length = 255)

 #To convert related model to string
    
def __self__(self)-> str:
    return self.title


class MenuItems(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    inventory = models.SmallIntegerField()
    #Creating a relational model
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default = 1)
    
   