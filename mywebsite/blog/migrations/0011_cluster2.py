# Generated by Django 2.2 on 2020-10-07 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20201007_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='cluster2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no2', models.CharField(max_length=10)),
                ('surat2', models.TextField(max_length=1000)),
                ('ayat2', models.CharField(max_length=20)),
                ('terjemah2', models.TextField(max_length=1000)),
            ],
        ),
    ]