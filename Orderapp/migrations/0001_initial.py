# Generated by Django 5.0.1 on 2024-02-05 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('reg_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.IntegerField()),
                ('add_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summa', models.DecimalField(decimal_places=2, max_digits=20)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orderapp.clientmodel')),
                ('products', models.ManyToManyField(to='Orderapp.productmodel')),
            ],
        ),
    ]
