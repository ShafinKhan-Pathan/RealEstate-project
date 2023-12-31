# Generated by Django 4.2.3 on 2023-07-14 22:31

import ckeditor.fields
from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_alter_asset_amenities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='amenities',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Balcony', 'Balcony'), ('Sun Room', 'Sun Room'), ('Outdoor Kitchen', 'Outdoor Kitchen'), ('Parking', 'Parking'), ('Air Condition', 'Air Condition'), ('Alarm System', 'Alarm System'), ('Tennis Court', 'Tennis Court'), ('VolleyBall Court', 'VolleyBall Court'), ('Home Theatre', 'Home Theatre'), ('Garden', 'Garden'), ('Children Play Area', 'Children Play Area'), ('Fitness CLub', 'Fitness CLub')], max_length=500),
        ),
        migrations.AlterField(
            model_name='asset',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
