# Generated by Django 3.1.7 on 2022-01-02 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigjob', '0002_bigjob_jobcat'),
    ]

    operations = [
        migrations.AddField(
            model_name='bigjob',
            name='holland1',
            field=models.CharField(default='I', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bigjob',
            name='holland2',
            field=models.CharField(default='I', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bigjob',
            name='holland3',
            field=models.CharField(default='I', max_length=1),
            preserve_default=False,
        ),
    ]
