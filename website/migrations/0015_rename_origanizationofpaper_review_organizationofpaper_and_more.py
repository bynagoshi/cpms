# Generated by Django 4.0.5 on 2022-07-10 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_rename_user_author_user_ref_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='OriganizationOfPaper',
            new_name='OrganizationOfPaper',
        ),
        migrations.AddField(
            model_name='review',
            name='paper_ref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.paper'),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer_ref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.reviewer'),
        ),
        migrations.AlterField(
            model_name='review',
            name='ClarityOfMainMessage',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='Complete',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='OverallRatingComments',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='PotentialForOralPresentationComments',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='WrittenDocumentComments',
            field=models.TextField(),
        ),
    ]
