# Generated by Django 4.0.2 on 2022-04-12 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song_rater_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]