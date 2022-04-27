# Generated by Django 2.2 on 2020-10-07 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200929_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='cluster1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=10)),
                ('surat', models.TextField(max_length=1000)),
                ('ayat', models.CharField(max_length=20)),
                ('terjemah', models.TextField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='dua',
        ),
        migrations.DeleteModel(
            name='satu',
        ),
    ]
