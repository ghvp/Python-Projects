# Generated by Django 4.1.4 on 2022-12-13 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus_name', models.CharField(blank=True, default='', max_length=60)),
                ('state', models.CharField(blank=True, default='', max_length=2)),
                ('campus_id', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
    ]