# Generated by Django 4.2.4 on 2023-10-06 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_formsubmission'),
    ]

    operations = [
        migrations.AddField(
            model_name='formsubmission',
            name='food',
            field=models.CharField(default='exit', max_length=200),
            preserve_default=False,
        ),
    ]
