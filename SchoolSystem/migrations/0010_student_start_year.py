# Generated by Django 4.0.3 on 2022-09-28 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolSystem', '0009_alter_student_graduated'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='start_year',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]