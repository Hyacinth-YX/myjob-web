# Generated by Django 3.1.7 on 2022-01-05 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='jobCat',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
