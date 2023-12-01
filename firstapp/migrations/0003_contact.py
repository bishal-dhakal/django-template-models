# Generated by Django 4.2.7 on 2023-11-30 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_selleradditional_customeradditional'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=10)),
                ('phone', models.IntegerField()),
                ('query', models.TextField()),
            ],
        ),
    ]
