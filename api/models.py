from django.contrib.auth.models import User
from django.db import models

#用户表
class AppUser(models.Model):
    name=models.CharField(max_length=50)
    class Meta:
        verbose_name="用户"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name


#类别
class Category(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name="类别"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

#商品表
class Product(models.Model):
    name = models.CharField(max_length=50)
    announcer=models.ForeignKey(AppUser,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    val=models.IntegerField(default=50)##值
    notval=models.IntegerField(default=50)##不值
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="商品"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

#商品爆料表
class UserProduct(models.Model):
   
    announcer = models.ForeignKey(AppUser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price_setting1=models.IntegerField(default=50)
    price_setting2=models.IntegerField(default=50)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name="爆料"
        verbose_name_plural=verbose_name
   
    
#评论表
class Comment(models.Model):
    comment_user=models.ForeignKey(AppUser,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    comment=models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="评论"
        verbose_name_plural=verbose_name

   


#商品收藏
class Subscribe(models.Model):
    subscriber=models.ForeignKey(AppUser,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price_setting=models.IntegerField(default=50)
    

    class Meta:
        verbose_name="关注"
        verbose_name_plural=verbose_name

 