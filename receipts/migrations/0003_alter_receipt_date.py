# Generated by Django 4.0.5 on 2022-06-16 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0002_alter_receipt_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
