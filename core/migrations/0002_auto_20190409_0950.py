# Generated by Django 2.2 on 2019-04-09 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('antique', 'Antique'), ('footwear', 'Footwear'), ('accessories', 'Accessories'), ('electronics', 'Electronics'), ('sports', 'Sports'), ('home appliances', 'Home Appliances'), ('books', 'Books'), ('furniture', 'Furniture'), ('tv & appliances', 'TV & Appliances')], max_length=100),
        ),
    ]
