# Generated by Django 5.0 on 2023-12-16 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='most_viwed',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
