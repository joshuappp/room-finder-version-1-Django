# Generated by Django 3.0.5 on 2020-04-26 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=60)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FindRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=40)),
                ('section', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='UploadRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=40)),
                ('section', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=60)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contact', models.IntegerField()),
                ('roomtype', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
