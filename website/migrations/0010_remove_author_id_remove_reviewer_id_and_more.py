# Generated by Django 4.0.5 on 2022-07-08 03:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0009_reviewer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='id',
        ),
        migrations.RemoveField(
            model_name='reviewer',
            name='id',
        ),
        migrations.AlterField(
            model_name='author',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
