# Generated by Django 4.2.2 on 2023-06-14 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_tag_alter_recipetag_recipe_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='tag',
            new_name='tags',
        ),
    ]
