# Generated by Django 4.0.3 on 2022-09-28 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolSystem', '0003_student_g_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduate_year',
            name='g_year',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
