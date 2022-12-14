# Generated by Django 3.1 on 2022-08-25 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the publisher.', max_length=50)),
                ('website', models.URLField(help_text='The website of the publisher.')),
                ('email', models.EmailField(help_text='The contact email of the publisher.', max_length=254)),
            ],
        ),
    ]
