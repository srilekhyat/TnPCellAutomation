# Generated by Django 3.2.7 on 2021-12-26 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningmaterial', '0003_auto_20211226_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concept',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
