# Generated by Django 4.0.3 on 2022-08-26 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('dob', models.DateField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('index_no', models.CharField(max_length=255)),
                ('level', models.CharField(default='L3', max_length=255)),
                ('father_names', models.CharField(max_length=255)),
                ('mother_name', models.CharField(max_length=255)),
                ('father_id', models.CharField(max_length=255)),
                ('father_tel', models.CharField(max_length=255)),
                ('mother_tel', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('sector', models.CharField(max_length=255)),
                ('village', models.CharField(max_length=255)),
                ('trade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolSystem.trade')),
            ],
        ),
    ]