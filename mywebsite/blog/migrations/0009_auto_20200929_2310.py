# Generated by Django 2.2 on 2020-09-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200929_2220'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tiga',
        ),
        migrations.RenameField(
            model_name='dua',
            old_name='ayat',
            new_name='ayatdua',
        ),
        migrations.RemoveField(
            model_name='dua',
            name='isi',
        ),
        migrations.AddField(
            model_name='dua',
            name='isidua',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
