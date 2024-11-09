# Generated by Django 5.1.2 on 2024-11-08 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantApp', '0002_rename_user_for_plant_used_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='category',
            field=models.CharField(choices=[('tree', 'Tree'), ('fruit', 'Fruit'), ('vegetables', 'Vegetables'), ('other', 'Other')], default='other', max_length=20),
        ),
    ]
