# Generated by Django 5.2.1 on 2025-06-02 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_hhoodie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Working',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('working_image', models.ImageField(upload_to='products')),
                ('working_name', models.CharField(max_length=100)),
                ('working_description', models.TextField()),
            ],
        ),
    ]
