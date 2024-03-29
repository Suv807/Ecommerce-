from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.TextField()
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100,default="")
    phone=models.CharField(max_length=50,default="")
    desc=models.TextField()

    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=800)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=100)
    phone=models.CharField(max_length=100,default="")


class OrderUpdate(models.Model):
    updated_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default=" ")
    updated_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.updated_desc[0:7]+"..."