# Generated by Django 4.0.2 on 2022-05-19 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortage', '0011_art_mara_marc_purchasing_group_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='zpp_md_stock',
            name='delivery_qty',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='zpp_md_stock',
            name='num_parcel',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
