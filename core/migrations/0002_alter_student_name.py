# Generated by Django 4.0.3 on 2022-04-05 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
