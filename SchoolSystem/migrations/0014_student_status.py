# Generated by Django 4.1.2 on 2022-10-10 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolSystem', '0013_alter_student_first_term_fee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
