# Generated by Django 4.2.7 on 2023-11-17 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_hospitaldetails_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReciverDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=100)),
                ('LastName', models.CharField(default='', max_length=100)),
                ('ContactNumber', models.CharField(default='', max_length=10)),
                ('LandlineNumber', models.CharField(default='', max_length=20)),
                ('Emailid', models.CharField(default='', max_length=100)),
                ('Address1', models.CharField(default='', max_length=100)),
                ('Address2', models.CharField(default='', max_length=100)),
                ('Gender', models.CharField(default='', max_length=10)),
                ('BloodGroupRequired', models.CharField(default='', max_length=100)),
                ('DateofBirth', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
