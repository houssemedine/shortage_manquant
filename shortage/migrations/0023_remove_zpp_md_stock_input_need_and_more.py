# Generated by Django 4.0.2 on 2022-05-23 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortage', '0022_remove_zpp_md_stock_uploaded_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zpp_md_stock',
            name='Input_need',
        ),
        migrations.RemoveField(
            model_name='zpp_md_stock',
            name='available_quantity',
        ),
    ]
