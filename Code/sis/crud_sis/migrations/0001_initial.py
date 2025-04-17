# Generated by Django 5.2 on 2025-04-17 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['last_name'],
                'permissions': [],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('is_published', models.BooleanField(default=False)),
                ('content', models.TextField()),
                ('instructors', models.ManyToManyField(to='crud_sis.instructor')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('courses', models.ManyToManyField(to='crud_sis.course')),
            ],
            options={
                'ordering': ['last_name'],
                'permissions': [],
            },
        ),
    ]
