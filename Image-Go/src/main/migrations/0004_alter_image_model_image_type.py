# Generated by Django 3.2.6 on 2021-08-18 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210818_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_model',
            name='image_Type',
            field=models.CharField(blank=True, choices=[('Free', 'Free'), ('Paid', 'Paid')], default='Free', max_length=5, null=True),
        ),
    ]
