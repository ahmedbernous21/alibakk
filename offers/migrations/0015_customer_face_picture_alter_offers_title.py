# Generated by Django 4.1.4 on 2023-02-18 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0014_alter_offers_devise_alter_offers_payment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='face_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='offers',
            name='title',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
