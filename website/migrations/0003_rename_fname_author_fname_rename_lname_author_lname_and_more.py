# Generated by Django 4.0.5 on 2022-07-07 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_paper_review_reviewer_author_authorid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='Fname',
            new_name='FName',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='Lname',
            new_name='LName',
        ),
        migrations.RenameField(
            model_name='reviewer',
            old_name='Fname',
            new_name='FName',
        ),
        migrations.RenameField(
            model_name='reviewer',
            old_name='Lname',
            new_name='LName',
        ),
        migrations.RemoveField(
            model_name='author',
            name='AuthorID',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='Active',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='AuthorID',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='PaperID',
        ),
        migrations.RemoveField(
            model_name='review',
            name='PaperID',
        ),
        migrations.RemoveField(
            model_name='review',
            name='ReviewID',
        ),
        migrations.RemoveField(
            model_name='review',
            name='ReviewerID',
        ),
        migrations.RemoveField(
            model_name='reviewer',
            name='ReviewerID',
        ),
    ]
