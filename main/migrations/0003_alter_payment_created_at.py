# Generated by Django 4.1.6 on 2023-12-26 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_group_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]