# Generated by Django 5.0.7 on 2024-08-05 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_absencebalance_delta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('sick_leave_per_month', models.FloatField(default=1)),
                ('casual_leave_per_month', models.FloatField(default=1.5)),
            ],
            options={
                'verbose_name_plural': 'Settings',
                'abstract': False,
            },
        ),
    ]
