# Generated by Django 3.2.7 on 2021-12-07 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Concept')),
                ('image', models.ImageField(default='defaultprofilepic.jpg', upload_to='learningmaterial')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100, verbose_name='Topic')),
                ('title1', models.CharField(max_length=500, verbose_name='Title1')),
                ('description1', models.CharField(max_length=3000, verbose_name='Description1')),
                ('title2', models.CharField(max_length=500, verbose_name='Title2')),
                ('description2', models.CharField(max_length=3000, verbose_name='Description2')),
                ('title3', models.CharField(max_length=500, verbose_name='Title3')),
                ('description3', models.CharField(max_length=3000, verbose_name='Description3')),
                ('concept', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='learningmaterial.concept', verbose_name='Concept')),
            ],
        ),
    ]
