# Generated by Django 4.2.5 on 2023-11-06 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_emailaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='email',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='myapp.emailaddress'),
        ),
    ]
