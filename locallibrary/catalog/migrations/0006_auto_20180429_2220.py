# Generated by Django 2.0.4 on 2018-04-29 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20180429_2158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_marked_returned', 'Set book as returned'),)},
        ),
    ]