# Generated by Django 4.1.7 on 2023-04-18 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_enrollment_trainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=185)),
                ('price', models.IntegerField(max_length=55)),
            ],
        ),
    ]
