# Generated by Django 4.0.3 on 2022-10-02 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolSystem', '0011_student_first_term_fee_student_second_term_fee_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fixed_Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_fixed_fee', models.CharField(blank=True, max_length=255, null=True)),
                ('second_fixed_fee', models.CharField(blank=True, max_length=255, null=True)),
                ('third_fixed_fee', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
