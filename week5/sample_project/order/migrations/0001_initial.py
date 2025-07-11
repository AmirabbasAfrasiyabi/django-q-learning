# Generated by Django 5.2.3 on 2025-06-23 14:25

import django.db.models.deletion
import order.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('property_one', models.FloatField(null=True)),
                ('price', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'info of order',
                'db_table': 'order_info',
                'ordering': ['-created_date'],
                'constraints': [models.UniqueConstraint(fields=('created_date', 'title'), name='created_title_unique')],
                'unique_together': {('created_date', 'title')},
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete', models.BooleanField(default=False)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'draft'), (1, 'submitted'), (2, 'rejected'), (3, 'accepted')], default=0)),
                ('info', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='order.orderinfo')),
            ],
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.FloatField(validators=[order.models.validate_between_zero_and_one])),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='order.ProductItem', to='order.product'),
        ),
    ]
