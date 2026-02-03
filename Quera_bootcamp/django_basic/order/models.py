from logging import exception

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

def validate_value_between_zero_and_one(value):
    if 0<= value <=1:
        return value
    raise exception('Value must be between 0 and 1')

class OrderStatus(models.IntegerChoices):
    draft = 0 , 'draft'
    submited = 1 , 'submited'
    rejected = 2 , 'rejected'
    accepted = 3 , 'accepted'


class OrderInfo(models.Model):
    title = models.CharField(max_length=100 , null=False , unique=True)
    created_date = models.DateTimeField(auto_now_add=True , db_index=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order_info'
        verbose_name='info of order'
        unique_together = ('title', 'created_date')
        ordering = ['-created_date']


class Order(models.Model):
    # order_id = models.AutoField(primary_key=True)
    complated = models.BooleanField(default=False , null=False)
    status = models.PositiveSmallIntegerField(choices=OrderStatus.choices, default=OrderStatus.draft )
    info = models.OneToOneField('OrderInfo' , on_delete=models.PROTECT)
    #second method to implement many to many
    product = models.ForeignKey('Product' , on_delete=models.PROTECT )


class Product(models.Model):
    name = models.CharField(max_length=100 , null=False , unique=True)
    price = models.PositiveSmallIntegerField(null=False)
    property_one = models.FloatField(null=False)


#first method to implement many to many
class ProductItem(models.Model):
    order = models.ForeignKey('Order' , on_delete=models.PROTECT)
    product = models.ForeignKey('Product' , on_delete=models.PROTECT)
    discount = models.FloatField(validators=[MinValueValidator(0) , MaxValueValidator(1)])

