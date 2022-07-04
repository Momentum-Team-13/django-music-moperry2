# Generated by Django 4.0.5 on 2022-07-04 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='name',
        ),
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
    ]