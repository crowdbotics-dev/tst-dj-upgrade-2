# Generated by Django 2.2.28 on 2022-10-12 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_hello'),
    ]

    operations = [
        migrations.AddField(
            model_name='hello',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
