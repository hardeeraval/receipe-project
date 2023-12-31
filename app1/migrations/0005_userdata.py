# Generated by Django 4.0.5 on 2023-07-07 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_datareceipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('confpw', models.CharField(max_length=100)),
            ],
        ),
    ]
