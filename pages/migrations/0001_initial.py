# Generated by Django 4.2.3 on 2023-07-12 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=255)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('facebook', models.URLField(max_length=100)),
                ('twitter', models.URLField(max_length=100)),
                ('insta', models.URLField(max_length=100)),
                ('linkedin', models.URLField(max_length=100)),
                ('createdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]