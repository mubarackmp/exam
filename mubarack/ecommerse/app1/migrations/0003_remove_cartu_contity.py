# Generated by Django 5.0.2 on 2024-02-10 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_cartu_contity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartu',
            name='contity',
        ),
    ]
