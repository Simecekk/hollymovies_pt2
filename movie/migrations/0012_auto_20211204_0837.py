# Generated by Django 3.2.9 on 2021-12-04 08:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_alter_cinemamoviescreening_sold_tickets'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='born_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 4, 8, 36, 51, 504713)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='director',
            name='born_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 4, 8, 37, 48, 454686)),
            preserve_default=False,
        ),
    ]
