# Generated by Django 3.2 on 2021-06-22 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.CharField(blank=True, db_index=True, max_length=140, null=True, verbose_name='Body'),
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Datetime'),
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(db_index=True, default='Anonymous', max_length=14, verbose_name='Name'),
        ),
    ]