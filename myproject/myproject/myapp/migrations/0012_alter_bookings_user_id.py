# Generated by Django 4.2.5 on 2023-11-06 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_bookings_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='user_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
    ]
