# Generated by Django 4.0.5 on 2022-07-08 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_remove_author_id_remove_reviewer_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='Password',
        ),
        migrations.RemoveField(
            model_name='reviewer',
            name='Password',
        ),
    ]
