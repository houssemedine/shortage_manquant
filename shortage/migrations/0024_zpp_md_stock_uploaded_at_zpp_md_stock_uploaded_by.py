# Generated by Django 4.0.2 on 2022-05-23 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortage', '0023_remove_zpp_md_stock_input_need_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='zpp_md_stock',
            name='uploaded_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='zpp_md_stock',
            name='uploaded_by',
            field=models.IntegerField(null=True),
        ),
    ]
