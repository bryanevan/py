# Generated by Django 4.2.5 on 2023-12-14 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_pic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['title']},
        ),
    ]
