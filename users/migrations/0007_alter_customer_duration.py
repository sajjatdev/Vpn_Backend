# Generated by Django 4.1 on 2022-09-02 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_durction_customer_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='duration',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
