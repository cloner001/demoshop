from django.db import models

# Create your models here.

class Product(models.Model):
    Product_id = models.AutoField
    Product_name = models.CharField(max_length=50)
    Product_description = models.CharField(max_length=300)
    Pub_date = models.DateTimeField()
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.Product_name

class Contact(models.Model):
    cont_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    email = models.EmailField(max_length=50)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key = True)
    Itemjson = models.CharField(max_length=5000)
    Name = models.CharField(max_length=50)
    Phone = models.IntegerField()
    Email = models.EmailField(max_length=50)
    Address = models.CharField(max_length=500)
    State = models.CharField(max_length=500)
    City = models.CharField(max_length=500)
    Zip_code = models.CharField(max_length=500)
    def __str__(self):
        return self.Name

class updateOrder(models.Model):

    update_id = models.AutoField(primary_key = True)
    order_id = models.IntegerField()
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
