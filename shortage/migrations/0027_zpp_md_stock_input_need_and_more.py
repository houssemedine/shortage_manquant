# Generated by Django 4.0.2 on 2022-05-23 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortage', '0026_zpp_md_stock_week_zpp_md_stock_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='zpp_md_stock',
            name='Input_need',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='zpp_md_stock',
            name='available_quantity',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
