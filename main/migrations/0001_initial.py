# Generated by Django 5.0.3 on 2024-04-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('author', models.CharField(max_length=200, verbose_name='Author')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
