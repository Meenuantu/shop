from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField()
    image=models.ImageField(upload_to='Category',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('ecomapp:products_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='Product',blank=True)
    stock=models.IntegerField()
    available_yes_no=models.BooleanField(default=True)
    created_on=models.DateField(auto_now_add=True)
    updated_on=models.DateField(auto_now=True)

    def get_url(self):
        return reverse('ecomapp:prodcatdetail',args=[self.category.slug,self.slug])