from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User


# Category
class Category(models.Model):
    title=models.CharField(max_length=100,verbose_name='نام دسته')
    # image=models.ImageField(upload_to="cat_imgs/")

    class Meta:
        verbose_name_plural='2. Categories'

    # def image_tag(self):
        # return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

# Brand
class Brand(models.Model):
    title=models.CharField(max_length=100,verbose_name='نام برند')
    # image=models.ImageField(upload_to="brand_imgs/")

    class Meta:
        verbose_name_plural='3. Brands'

    def __str__(self):
        return self.title

# Color
class Metraj(models.Model):
    title=models.CharField(max_length=100,verbose_name='متراژ')

    class Meta:
        verbose_name_plural='4. Metraj'

    # def color_bg(self):
        # return mark_safe('<div style="width:30px; height:30px; background-color:%s"></div>' % (self.color_code))

    def __str__(self):
        return self.title

# Size
class Size(models.Model):
    title=models.CharField(max_length=100,verbose_name='سایز')

    class Meta:
        verbose_name_plural='5. Sizes'

    def __str__(self):
        return self.title



    

# Product Model
class Product(models.Model):
    title=models.CharField(max_length=400,verbose_name='نام محصول',null=False,blank=False,db_index=True)
    slug=models.CharField(max_length=400,verbose_name='نامک',null=False,blank=False,unique=True,db_index=True)
    short_discration = models.CharField(max_length=200,verbose_name='توظیحات کوتاه',null=True,blank=True)
    detail=models.TextField(verbose_name='جزییات محصول')
    specs=models.TextField(verbose_name='مشخصات فنی',null=True,blank=True)
    category=models.ManyToManyField(Category,verbose_name='دسته بندی',null=True,blank=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,verbose_name='برند محصول',null=True,blank=True)
    colors=models.CharField(verbose_name=' ,رنگ محصول | جدا کننده با ',max_length=800)
    image_1= models.ImageField(upload_to="product_imgs/",null=True,blank=True,verbose_name='عکس محصول.1')
    image_2= models.ImageField(upload_to="product_imgs/",null=True,blank=True,verbose_name='عکس محصول.2')
    image_3= models.ImageField(upload_to="product_imgs/",null=True,blank=True,verbose_name='عکس محصول.3')
    image_4= models.ImageField(upload_to="product_imgs/",null=True,blank=True,verbose_name='عکس محصول.4')
    price = models.FloatField(verbose_name='قیمت محصول',null=True,blank=True)
    status=models.BooleanField(default=True,verbose_name='فعال/غیرفعال')
    is_delete=models.BooleanField(default=False,verbose_name='حذف شده/حذف نشده')
    
    


    class Meta:
        verbose_name_plural='6. Products'

    def __str__(self):
        return self.title

# Product Attribute
class ProductAttribute(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='نام محصول',null=True,blank=True)
    metraj = models.ForeignKey(Metraj,on_delete=models.CASCADE,verbose_name='متراژ',null=True,blank=True)    
    size=models.ForeignKey(Size,on_delete=models.CASCADE,verbose_name='سایز',null=True,blank=True)
    price=models.PositiveIntegerField(default=0,verbose_name='قیمت',null=True,blank=True)
    

    class Meta:
        verbose_name_plural='7. ProductAttributes'

    def __str__(self):
        return self.product.title



# images
class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')
    image = models.ImageField(upload_to='product_imgs/',null=True,blank=True,verbose_name='عکس محصول')

    class Meta:
        verbose_name_plural = '1. Images'

    def __str__(self):
        return self.product.title
