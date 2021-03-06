# Generated by Django 4.0.5 on 2022-07-06 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=50)),
                ('MiddleInitial', models.CharField(max_length=1)),
                ('Lname', models.CharField(max_length=50)),
                ('Affliation', models.CharField(max_length=50)),
                ('Department', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=2)),
                ('Zipcode', models.CharField(max_length=10)),
                ('PhoneNumber', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
