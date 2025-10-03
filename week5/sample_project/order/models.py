from django.db import models
from django.db.models import UniqueConstraint

def validate_between_zero_and_one(value):
    if 0 <= value <= 1:
        return value
    raise Exception('Value is not between 0 & 1')

# Create your models here.
class OrderInfo(models.Model):
    title = models.CharField(max_length=32, null=False, unique=True)
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order_info'
        verbose_name = 'info of order'
        # First method to make two fields unique together
        unique_together = ['created_date', 'title']
        # Second method to make two fields unique together
        constraints = [UniqueConstraint(fields=['created_date', 'title'], name='created_title_unique')]
        ordering = ['-created_date']


class Order(models.Model):
    class OrderStatus(models.IntegerChoices):
        draft = 0, 'draft'
        submitted = 1, 'submitted'
        rejected = 2, 'rejected'
        accepted = 3, 'accepted'

    complete = models.BooleanField(default=False, null=False)
    status = models.PositiveSmallIntegerField(choices=OrderStatus.choices, default=OrderStatus.draft)
    info = models.OneToOneField(to='OrderInfo', on_delete=models.PROTECT)
    # Second method to implement many-to-many relation
    products = models.ManyToManyField(to='Product', through='ProductItem')

class Product(models.Model):
    name = models.CharField(max_length=64, null=False)
    property_one = models.FloatField(null=True)
    price = models.PositiveSmallIntegerField(null=False)


 # First method to implement many-to-many relation
class ProductItem(models.Model):
    order = models.ForeignKey(to='Order', on_delete=models.CASCADE)
    product = models.ForeignKey(to='Product', on_delete=models.PROTECT)
    discount = models.FloatField(validators=[validate_between_zero_and_one])
