# Generated by Django 4.1.7 on 2023-03-13 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_todo_tittle'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='body',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]