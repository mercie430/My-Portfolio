# Generated by Django 4.2.5 on 2025-04-05 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='about')),
                ('header', models.CharField(max_length=150)),
                ('desc1', models.TextField()),
                ('desc2', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('age', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('occupation', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
            ],
        ),
    ]
