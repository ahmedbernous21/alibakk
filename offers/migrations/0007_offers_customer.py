# Generated by Django 4.1.4 on 2023-01-26 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0006_payment_rename_profile_pic_customer_card_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='offers',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='offers.customer'),
        ),
    ]
