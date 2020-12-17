from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

db = models
class Product(models.Model):

    __tablename__ = 'product'
    product_id = db.IntegerField(primary_key=True)
    title = db.CharField(max_length=100)
    description = db.CharField(max_length=200)
    sale_price = db.FloatField()
    logo = db.CharField(max_length=100)
    featured = db.CharField(max_length=100, default='ok')
    status = db.CharField(max_length=100,null=True)
    add_timestamp = db.DateTimeField(auto_now_add=True)
    number_of_view = db.IntegerField(default=0)
    category = db.IntegerField(default='')
    sub_category = db.IntegerField( null=True, default='')
    additional_fields = db.CharField(max_length=100,null=True, default='')

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    __tablename__ = "sub_category"

    sub_category_id = db.IntegerField(null=False,primary_key= True)
    sub_category_name = db.CharField(max_length=100)
    category = db.CharField(max_length=100)
    brand = db.CharField(max_length=2000,null=False,default='[]')
    digital = db.CharField(max_length=100,default=0)
    banner = db.CharField(max_length=100)
    affiliation = db.IntegerField(default=0)
    affiliation_points = db.FloatField(null=False,default=0)

class Category(db.Model):
    __tablename__ = "category"

    category_id = db.IntegerField(null=False,primary_key=True)
    category_name = db.CharField(max_length=100)
    description = db.CharField(max_length=100)
    digital = db.CharField(max_length=10,default='')
    banner = db.CharField(max_length=100)
    data_brands = db.CharField(max_length=100)
    data_vendors = db.CharField(max_length=100)
    data_subdets = db.CharField(max_length=100)