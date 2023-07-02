from django.db import models
import random
# Create your models here.
class Solution(models.Model):
    id = models.AutoField(primary_key=True)
    public_id = models.CharField(max_length=100,default="default")
    title = models.CharField(max_length=100)
    description = models.TextField()
    sol_img = models.ImageField(upload_to='static/solution', default="")
    spec_img = models.ImageField(upload_to='static/solution', default="",null=True,blank=True)

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        # Generate the public ID based on field1 and field2
        public_id_str = f"{self.title.replace(' ', '-')}"
        self.public_id = public_id_str.lower()

        super().save(*args, **kwargs)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    public_id = models.CharField(max_length=100,default="default")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000,null=True,blank=True)
    cat_img = models.ImageField(upload_to='static/category', default="")

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        # Generate the public ID based on field1 and field2
        public_id_str = f"{self.title.replace(' ', '-')}"
        self.public_id = public_id_str.lower()

        super().save(*args, **kwargs)


class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    public_id = models.CharField(max_length=100,default="default")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000,null=True,blank=True)
    subcat_img = models.ImageField(upload_to='static/subcategory', default="")
    category =  models.ForeignKey(Category, on_delete=models.CASCADE,default="")

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        # Generate the public ID based on field1 and field2
        public_id_str = f"{self.title.replace(' ', '-')}"
        self.public_id = public_id_str.lower()

        super().save(*args, **kwargs)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=100)
    public_id = models.CharField(max_length=100,default="default")
    prod_img = models.ImageField(upload_to='static/product', default="")
    prod_spec = models.ImageField(upload_to='static/specs', default="",null=True,blank=True)
    prod_manual = models.FileField(upload_to='static/manual', default="",null=True,blank=True)
    prod_brocher = models.FileField(upload_to='static/brocher', default="",null=True,blank=True)
    prod_desc = models.CharField(max_length=1000,null=True,blank=True)
    prod_subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,default="")
    prod_price = models.IntegerField(default=0,null=True,blank=True)
    prod_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.prod_name

    def save(self, *args, **kwargs):
        # Generate the public ID based on field1 and field2
        public_id_str = f"{self.prod_name.replace(' ', '-')}"
        self.public_id = public_id_str.lower()

        super().save(*args, **kwargs)
