# Generated by Django 4.2.5 on 2023-09-19 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
