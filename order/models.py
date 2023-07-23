from django.db import models



class Order(models.Model):
    size = models.CharField(max_length=400,null=True,blank=True,verbose_name='سایز')
    metraj = models.CharField(max_length=400,null=True,blank=True,verbose_name='متراژ')
    colore = models.CharField(max_length=400,null=True,blank=True,verbose_name='رنگ')
    name = models.CharField(max_length=400,null=True,blank=True,verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=500,null=True,blank=True,verbose_name='آدرس ایمیل')
    phone = models.CharField(max_length=400,null=True,blank=True,verbose_name='شماره تماس')
    home_phone = models.CharField(max_length=400,null=True,blank=True,verbose_name='شماره تماس')
    name_products = models.CharField(max_length=400,null=True,blank=True,verbose_name='محصول')
    addr = models.CharField(max_length=1000,null=True,blank=True,verbose_name='آدرس')
    national_code = models.CharField(max_length=100,null=True,blank=True,verbose_name='کد ملی')
    postal_code = models.CharField(max_length=100,null=True,blank=True,verbose_name='آدرس پستی')
    transport_1 = models.BooleanField(null=True,blank=True,verbose_name='باربری',default=True)
    transport_1 = models.BooleanField(null=True,blank=True,verbose_name='پیک فقط برای شهر تهران',default=False)

    class Meta:
        verbose_name_plural='8. سفارشات'

    def __str__(self):
        return self.name_products        