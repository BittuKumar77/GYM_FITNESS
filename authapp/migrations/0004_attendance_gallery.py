# Generated by Django 4.1.7 on 2023-04-18 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_membershipplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Selectdate', models.DateTimeField(auto_now_add=True)),
                ('phonenumber', models.CharField(max_length=15)),
                ('Login', models.CharField(max_length=200)),
                ('Logout', models.CharField(max_length=200)),
                ('SelectWorkout', models.CharField(max_length=200)),
                ('TrainedBy', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='gallery')),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
