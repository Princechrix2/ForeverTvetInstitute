# Generated by Django 4.1.2 on 2022-10-11 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolSystem', '0014_student_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fixed_Fee_Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_fixed_fee_day', models.CharField(blank=True, max_length=255, null=True)),
                ('second_fixed_fee_day', models.CharField(blank=True, max_length=255, null=True)),
                ('third_fixed_fee_day', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]