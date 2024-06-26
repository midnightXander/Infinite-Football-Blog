# Generated by Django 4.2.6 on 2024-03-08 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_blogpost_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='bodyImage',
            field=models.ImageField(blank=True, upload_to='posts_images/'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='cover_image',
            field=models.ImageField(upload_to='posts_images/'),
        ),
    ]
