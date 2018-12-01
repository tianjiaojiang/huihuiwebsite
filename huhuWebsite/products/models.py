from django.db import models


# Create your models here.
class Category(models.Model):
    cat_id = models.CharField(max_length=100, primary_key=True)
    cat_name = models.CharField(max_length=30)
    parent_id = models.CharField(max_length=100)
    sort = models.IntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()


class AttributeKey(models.Model):
    attr_id = models.CharField(max_length=100, primary_key=True)
    attr_name = models.CharField(max_length=30)
    cat_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    sort = models.IntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()


class AttributeValue(models.Model):
    value_id = models.CharField(max_length=100,primary_key=True)
    value_name = models.CharField(max_length=30)
    key_id = models.ForeignKey(AttributeKey, on_delete=models.SET_NULL, null=True)
    sort = models.IntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()


class Product(models.Model):
    product_id = models.CharField(max_length=100, primary_key=True)
    product_name = models.CharField(max_length=100)
    product_model = models.CharField(max_length=30)
    cat_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    thumb_url = models.CharField(max_length=100)
    img_urls = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    prod_attr = models.CharField(max_length=500)
    sort = models.IntegerField()
    status = models.IntegerField(default=1)
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()


class ProductAttribute(models.Model):
    ProdAttr_id = models.AutoField(primary_key=True)
    prod_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    attr_key = models.ForeignKey(AttributeKey, on_delete=models.CASCADE)
    attr_value = models.ForeignKey(AttributeValue,on_delete=models.CASCADE)
    sort = models.IntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()




